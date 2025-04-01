import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

class TestFTPConnection:
    def test_successful_connection(self):
        # Mocking FTP connection to avoid actual network calls
        with patch('ftplib.FTP') as mock_ftp:
            # Setup mock objects
            mock_instance = MagicMock()
            mock_instance.login.return_value = "220 Welcome to the server"
            mock_ftp.return_value = mock_instance

            # Call the function
            connection, welcome_msg = establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass'
            )

            # Assertions
            assert connection == mock_instance
            assert welcome_msg == "220 Welcome to the server"
            mock_instance.connect.assert_called_once_with(host='test.server.com', port=21)
            mock_instance.login.assert_called_once_with(user='testuser', passwd='testpass')

    def test_missing_parameters(self):
        # Test missing parameters raise ValueError
        with pytest.raises(ValueError, match="Host, username, and password are required"):
            establish_ftp_connection(host='', username='', password='')

    def test_connection_failure(self):
        # Test connection failures during connection
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            # Simulate connection error
            mock_instance.connect.side_effect = ftplib.error_perm("Connection failed")
            mock_ftp.return_value = mock_instance

            with pytest.raises(ConnectionError, match="FTP Connection Error"):
                establish_ftp_connection(
                    host='invalid.server.com', 
                    username='baduser', 
                    password='badpass'
                )

    def test_login_failure(self):
        # Test login failures
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            # Connection succeeds, but login fails
            mock_instance.login.side_effect = ftplib.error_perm("Login failed")
            mock_ftp.return_value = mock_instance

            with pytest.raises(ConnectionError, match="FTP Login Error"):
                establish_ftp_connection(
                    host='test.server.com', 
                    username='baduser', 
                    password='badpass'
                )

    def test_custom_port(self):
        # Test connection with custom port
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance

            establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass', 
                port=2121
            )

            mock_instance.connect.assert_called_once_with(host='test.server.com', port=2121)

    def test_custom_timeout(self):
        # Test connection with custom timeout
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance

            establish_ftp_connection(
                host='test.server.com', 
                username='testuser', 
                password='testpass', 
                timeout=10
            )

            assert mock_ftp.call_args[1]['timeout'] == 10