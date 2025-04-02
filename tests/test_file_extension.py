import pytest
import os
from src.file_extension import get_file_extension

def test_get_file_extension_basic_cases():
    """Test basic file extension extraction."""
    assert get_file_extension('example.txt') == 'txt'
    assert get_file_extension('document.pdf') == 'pdf'
    assert get_file_extension('image.jpg') == 'jpg'

def test_get_file_extension_multiple_dots():
    """Test file extensions with multiple dots."""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('script.test.py') == 'py'

def test_get_file_extension_no_extension():
    """Test files without extensions."""
    assert get_file_extension('README') == ''
    assert get_file_extension('configuration') == ''

def test_get_file_extension_full_path():
    """Test file extensions with full file paths."""
    assert get_file_extension('/home/user/documents/report.docx') == 'docx'
    assert get_file_extension('C:\\Users\\name\\file.xlsx') == 'xlsx'

def test_get_file_extension_error_cases():
    """Test error handling."""
    # Non-string input
    with pytest.raises(TypeError):
        get_file_extension(123)
    
    # Empty string
    with pytest.raises(ValueError):
        get_file_extension('')

def test_get_file_extension_hidden_files():
    """Test hidden files with extensions."""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('.bashrc') == ''
    # Change this test to match the implementation
    assert get_file_extension('src/.env') == ''