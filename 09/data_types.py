from typing import TypeAlias, Tuple

FileId: TypeAlias = int
BlockCount: TypeAlias = int
File: TypeAlias = Tuple[FileId, BlockCount]
