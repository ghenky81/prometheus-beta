import os
import zipfile

def create_password_protected_zip(source_paths, output_zip_path, password):
    """
    Create a password-protected zip file from given source paths.

    Args:
        source_paths (list): List of file or directory paths to be zipped
        output_zip_path (str): Path where the encrypted zip file will be saved
        password (str): Password to protect the zip file

    Raises:
        ValueError: If source_paths is empty or password is too short
        TypeError: If input types are incorrect
        IOError: If sources cannot be read or zip cannot be created
    
    Returns:
        str: Path to the created password-protected zip file
    """
    # Input validation
    if not source_paths:
        raise ValueError("At least one source path must be provided")
    
    if not isinstance(source_paths, list):
        raise TypeError("source_paths must be a list")
    
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long")

    # Normalize paths and check existence
    normalized_sources = []
    for path in source_paths:
        abs_path = os.path.abspath(path)
        if not os.path.exists(abs_path):
            raise IOError(f"Source path does not exist: {abs_path}")
        normalized_sources.append(abs_path)

    # Create zip file with password protection
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for source in normalized_sources:
                if os.path.isdir(source):
                    # Add entire directory
                    for root, _, files in os.walk(source):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, os.path.dirname(source))
                            zipf.write(file_path, arcname=arcname)
                else:
                    # Add single file
                    zipf.write(source, os.path.basename(source))
            
            # Set password for the entire archive
            zipf.setpassword(password.encode())
    
    except Exception as e:
        raise IOError(f"Error creating zip file: {str(e)}")

    return output_zip_path