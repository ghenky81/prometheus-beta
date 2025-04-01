import io
import sys
import pytest
from src.colored_logger import ColoredLogger

class TestColoredLogger:
    def test_default_log(self, capsys):
        """Test default logging behavior."""
        ColoredLogger.log("Test message")
        captured = capsys.readouterr()
        assert "Test message" in captured.out
        assert "\x1b[47m" in captured.out  # White background
        assert "\x1b[30m" in captured.out  # Black text
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        color_codes = {
            'red': '\x1b[41m', 'green': '\x1b[42m', 'yellow': '\x1b[43m', 
            'blue': '\x1b[44m', 'magenta': '\x1b[45m', 'cyan': '\x1b[46m', 
            'white': '\x1b[47m'
        }
        for color in colors:
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            assert "Color test" in captured.out
            assert color_codes[color] in captured.out
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\033[31m')
        captured = capsys.readouterr()
        assert "Test" in captured.out
        assert "\x1b[47m" in captured.out  # White background
        assert "\x1b[31m" in captured.out  # Red text
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        assert "Debug message" in captured.out
        assert "\x1b[44m" in captured.out   # Blue background for debug
        
        assert "Warning message" in captured.out
        assert "\x1b[43m" in captured.out   # Yellow background for warning
        
        assert "Error message" in captured.out
        assert "\x1b[41m" in captured.out   # Red background for error
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        content = output.read()
        assert "File test" in content
        output.close()