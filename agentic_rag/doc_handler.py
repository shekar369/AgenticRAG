"""Utility functions to handle .doc format documents."""

import os
from typing import Optional

try:
    import textract  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    textract = None


def doc_to_text(path: str) -> str:
    """Return the extracted text from a .doc file.

    Parameters
    ----------
    path: str
        Path to the .doc file.

    Raises
    ------
    ImportError
        If the optional ``textract`` dependency is not installed.
    FileNotFoundError
        If the file does not exist.
    """
    if textract is None:
        raise ImportError(
            "textract is required to read .doc files. Install it with 'pip install textract'."
        )

    if not os.path.exists(path):
        raise FileNotFoundError(path)

    text_bytes = textract.process(path)
    return text_bytes.decode("utf-8")

