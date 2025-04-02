import os

def get_file_extension(file_path):
    """
    Get the file extension of a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (without the dot) or an empty string if no extension exists.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is an empty string.
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check for empty string
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Split the full path into directory and filename
    _, filename = os.path.split(file_path)
    
    # If filename is just a dot-prefixed name without an extension
    if filename.startswith('.') and '.' not in filename[1:]:
        return ''
    
    # Get the last part after the last dot
    parts = filename.split('.')
    return parts[-1] if len(parts) > 1 else ''