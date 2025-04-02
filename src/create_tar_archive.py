import os
import tarfile
from typing import Union, Optional


def create_tar_archive(source_dir: str, 
                       archive_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a given directory.

    Args:
        source_dir (str): Path to the source directory to be archived
        archive_path (Optional[str], optional): Path for the output tar archive. 
            If not provided, will be generated based on source directory. 
        compression (str, optional): Compression type. 
            Defaults to 'gz'. Supports 'gz', 'bz2', and None.

    Returns:
        str: Path to the created tar archive

    Raises:
        ValueError: If source directory does not exist or is not a directory
        ValueError: If invalid compression type is specified
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory {source_dir} does not exist")
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source {source_dir} is not a directory")

    # Validate compression type
    valid_compressions = {'gz', 'bz2', None}
    if compression not in valid_compressions:
        raise ValueError(f"Invalid compression type. Must be one of {valid_compressions}")

    # Determine archive path
    if archive_path is None:
        dir_name = os.path.basename(source_dir)
        archive_path = f"{source_dir}.tar{'.gz' if compression == 'gz' else '.bz2' if compression == 'bz2' else ''}"

    # Create tar archive
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(archive_path, mode) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    return archive_path