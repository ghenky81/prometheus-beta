import ftplib
from typing import Optional, Tuple

def establish_ftp_connection(
    host: str, 
    username: str, 
    password: str, 
    port: int = 21, 
    timeout: int = 30
) -> Tuple[ftplib.FTP, str]:
    """
    Establish a connection to an FTP server.

    Args:
        host (str): Hostname or IP address of the FTP server
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): FTP server port. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        Tuple[ftplib.FTP, str]: A tuple containing the FTP connection object and welcome message

    Raises:
        ValueError: If any required connection parameters are missing
        ConnectionError: For various FTP-related connection errors
    """
    # Validate input parameters
    if not host or not username or not password:
        raise ValueError("Host, username, and password are required")

    try:
        # Establish FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        try:
            ftp.connect(host=host, port=port)
        except ftplib.all_errors as connect_err:
            raise ConnectionError(f"FTP Connection Error: {str(connect_err)}")
        
        try:
            # Authenticate
            welcome_msg = ftp.login(user=username, passwd=password)
        except ftplib.all_errors as login_err:
            raise ConnectionError(f"FTP Login Error: {str(login_err)}")
        
        return ftp, welcome_msg
    except Exception as e:
        raise ConnectionError(f"FTP Connection Error: {str(e)}")