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
    
    # Use basename to handle paths
    filename = os.path.basename(file_path)
    
    # Special case: if filename starts with a dot and has no other dots, it's not an extension
    if filename.startswith('.') and '.' not in filename[1:]:
        return ''
    
    # Use os.path.splitext to handle filenames with complex extensions
    _, extension = os.path.splitext(filename)
    
    # Remove the leading dot and return
    return extension.lstrip('.')