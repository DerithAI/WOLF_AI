"""
WOLF_AI Core - The Pack Consciousness
"""

__version__ = "0.2.0"
__codename__ = "Command Center"

PACK_MEMBERS = ["alpha", "scout", "hunter", "oracle", "shadow"]
FREQUENCIES = ["low", "medium", "high", "AUUUU"]

from .wolf import (
    Wolf,
    Alpha,
    Scout,
    Hunter,
    Oracle,
    Shadow,
    create_wolf,
    WOLF_CLASSES
)

from .pack import (
    Pack,
    get_pack,
    awaken_pack,
    reset_pack
)

__all__ = [
    # Version
    "__version__", "__codename__",
    "PACK_MEMBERS", "FREQUENCIES",

    # Wolves
    "Wolf", "Alpha", "Scout", "Hunter", "Oracle", "Shadow",
    "create_wolf", "WOLF_CLASSES",

    # Pack
    "Pack", "get_pack", "awaken_pack", "reset_pack"
]
