"""DNS Opcodes."""
import dns.enum
import dns.exception

class Opcode(dns.enum.IntEnum):
    QUERY = 0
    IQUERY = 1
    STATUS = 2
    NOTIFY = 4
    UPDATE = 5

class UnknownOpcode(dns.exception.DNSException):
    """An DNS opcode is unknown."""

def from_text(text: str) -> Opcode:
    """Convert text into an opcode.

    *text*, a ``str``, the textual opcode

    Raises ``dns.opcode.UnknownOpcode`` if the opcode is unknown.

    Returns an ``int``.
    """
    pass

def from_flags(flags: int) -> Opcode:
    """Extract an opcode from DNS message flags.

    *flags*, an ``int``, the DNS flags.

    Returns an ``int``.
    """
    pass

def to_flags(value: Opcode) -> int:
    """Convert an opcode to a value suitable for ORing into DNS message
    flags.

    *value*, an ``int``, the DNS opcode value.

    Returns an ``int``.
    """
    pass

def to_text(value: Opcode) -> str:
    """Convert an opcode to text.

    *value*, an ``int`` the opcode value,

    Raises ``dns.opcode.UnknownOpcode`` if the opcode is unknown.

    Returns a ``str``.
    """
    pass

def is_update(flags: int) -> bool:
    """Is the opcode in flags UPDATE?

    *flags*, an ``int``, the DNS message flags.

    Returns a ``bool``.
    """
    pass
QUERY = Opcode.QUERY
IQUERY = Opcode.IQUERY
STATUS = Opcode.STATUS
NOTIFY = Opcode.NOTIFY
UPDATE = Opcode.UPDATE