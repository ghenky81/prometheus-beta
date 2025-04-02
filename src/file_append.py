def append_to_file(file_path, text):
    """
    Append text to an existing file.

    Args:
        file_path (str): The path to the file to append to.
        text (str): The text to append to the file.

    Raises:
        TypeError: If file_path or text is not a string.
        ValueError: If file_path is an empty string.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Validate file path is not empty
    if not file_path.strip():
        raise ValueError("file_path cannot be an empty string")
    
    # Append text to the file
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except IOError as e:
        # Catch and re-raise any file operation errors with a more descriptive message
        raise IOError(f"Error appending to file {file_path}: {str(e)}")