import os
import tarfile
import pytest
import tempfile
import shutil

from src.create_tar_archive import create_tar_archive


@pytest.fixture
def sample_directory():
    """Create a temporary directory with some sample files for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        
        # Create a subdirectory
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'subdir', 'file3.txt'), 'w') as f:
            f.write('Test content 3')
        
        yield temp_dir


def test_create_tar_archive_default(sample_directory):
    """Test creating a tar.gz archive with default settings."""
    archive_path = create_tar_archive(sample_directory)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert len(members) > 0  # Archive is not empty
        assert os.path.basename(sample_directory) in members  # Root directory included


def test_create_tar_archive_custom_path(sample_directory):
    """Test creating a tar archive with a custom path."""
    custom_path = os.path.join(tempfile.gettempdir(), 'custom_archive.tar.bz2')
    archive_path = create_tar_archive(sample_directory, 
                                      archive_path=custom_path, 
                                      compression='bz2')
    
    # Verify archive was created at the specified path
    assert os.path.exists(custom_path)
    assert custom_path == archive_path
    
    # Verify archive contents
    with tarfile.open(custom_path, 'r:bz2') as tar:
        members = tar.getnames()
        assert len(members) > 0  # Archive is not empty


def test_create_tar_archive_no_compression(sample_directory):
    """Test creating an uncompressed tar archive."""
    archive_path = create_tar_archive(sample_directory, compression=None)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:') as tar:
        members = tar.getnames()
        assert len(members) > 0  # Archive is not empty


def test_create_tar_archive_invalid_directory():
    """Test error handling for non-existent directory."""
    with pytest.raises(ValueError, match="does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')


def test_create_tar_archive_not_directory():
    """Test error handling when source is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="is not a directory"):
            create_tar_archive(temp_file.name)


def test_create_tar_archive_invalid_compression(sample_directory):
    """Test error handling for invalid compression type."""
    with pytest.raises(ValueError, match="Invalid compression type"):
        create_tar_archive(sample_directory, compression='invalid')