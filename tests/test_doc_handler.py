import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agentic_rag import doc_to_text
import pytest


def test_doc_to_text_missing_file():
    with pytest.raises(FileNotFoundError):
        doc_to_text('nonexistent.doc')


def test_doc_to_text_requires_textract(monkeypatch, tmp_path):
    # simulate missing textract
    monkeypatch.setitem(sys.modules, 'textract', None)
    monkeypatch.setattr('agentic_rag.doc_handler.textract', None, raising=False)
    test_file = tmp_path / 'empty.doc'
    test_file.write_bytes(b'')
    with pytest.raises(ImportError):
        doc_to_text(str(test_file))
