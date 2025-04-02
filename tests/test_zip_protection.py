import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_protection import create_password_protected_zip

def test_create_single_file_zip():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Create zip
        output_zip = os.path.join(temp_dir, 'protected.zip')
        result_path = create_password_protected_zip([test_file_path], output_zip, 'password123')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Try to open zip with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.extractall(path=temp_dir, pwd=b'password123')
            extracted_file = os.path.join(temp_dir, 'test_file.txt')
            assert os.path.exists(extracted_file)
            with open(extracted_file, 'r') as f:
                assert f.read() == 'Test content'

def test_create_directory_zip():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test directory with files
        test_dir = os.path.join(temp_dir, 'test_dir')
        os.makedirs(test_dir)
        
        # Create some files in the directory
        with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
            f.write('Content 1')
        with open(os.path.join(test_dir, 'file2.txt'), 'w') as f:
            f.write('Content 2')
        
        # Create zip
        output_zip = os.path.join(temp_dir, 'dir_protected.zip')
        result_path = create_password_protected_zip([test_dir], output_zip, 'password456')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Create extraction directory
        extract_dir = os.path.join(temp_dir, 'extracted')
        os.makedirs(extract_dir)
        
        # Try to open zip with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.extractall(path=extract_dir, pwd=b'password456')
            
            # Verify extracted files
            assert os.path.exists(os.path.join(extract_dir, 'test_dir', 'file1.txt'))
            assert os.path.exists(os.path.join(extract_dir, 'test_dir', 'file2.txt'))

def test_empty_source_paths():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_zip = os.path.join(temp_dir, 'empty.zip')
        
        with pytest.raises(ValueError, match="At least one source path must be provided"):
            create_password_protected_zip([], output_zip, 'password')

def test_invalid_source_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_zip = os.path.join(temp_dir, 'invalid.zip')
        
        with pytest.raises(IOError, match="Source path does not exist"):
            create_password_protected_zip(['/nonexistent/path'], output_zip, 'password')

def test_short_password():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        output_zip = os.path.join(temp_dir, 'short_pass.zip')
        
        with pytest.raises(ValueError, match="Password must be at least 4 characters long"):
            create_password_protected_zip([test_file_path], output_zip, '123')

def test_multiple_sources():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple test files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('Content 1')
        with open(file2_path, 'w') as f:
            f.write('Content 2')
        
        # Create zip
        output_zip = os.path.join(temp_dir, 'multi_file.zip')
        result_path = create_password_protected_zip([file1_path, file2_path], output_zip, 'password789')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Create extraction directory
        extract_dir = os.path.join(temp_dir, 'extracted')
        os.makedirs(extract_dir)
        
        # Try to open zip with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.extractall(path=extract_dir, pwd=b'password789')
            
            # Verify extracted files
            assert os.path.exists(os.path.join(extract_dir, 'file1.txt'))
            assert os.path.exists(os.path.join(extract_dir, 'file2.txt'))