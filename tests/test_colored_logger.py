import io
import sys
import pytest
from src.colored_logger import ColoredLogger

class TestColoredLogger:
    def test_default_log(self, capsys):
        """Test default logging behavior."""
        ColoredLogger.log("Test message")
        captured = capsys.readouterr()
        output = captured.out.strip()
        assert output == "\x1b[47m\x1b[30mTest message\x1b[0m"
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = {
            'red': '\x1b[41m', 'green': '\x1b[42m', 'yellow': '\x1b[43m', 
            'blue': '\x1b[44m', 'magenta': '\x1b[45m', 'cyan': '\x1b[46m', 
            'white': '\x1b[47m'
        }
        color_text_map = {
            'red': '\x1b[37m', 'green': '\x1b[30m', 'yellow': '\x1b[30m', 
            'blue': '\x1b[37m', 'magenta': '\x1b[37m', 'cyan': '\x1b[30m', 
            'white': '\x1b[30m'
        }
        
        for color, color_code in colors.items():
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            output = captured.out.strip()
            
            assert output == f"{color_code}{color_text_map[color]}Color test\x1b[0m"
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\x1b[31m')
        captured = capsys.readouterr()
        output = captured.out.strip()
        
        assert output == "\x1b[47m\x1b[31mTest\x1b[0m"
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        outputs = captured.out.strip().split('\n')
        
        assert outputs[0] == "\x1b[44m\x1b[37mDebug message\x1b[0m"
        assert outputs[1] == "\x1b[43m\x1b[30mWarning message\x1b[0m"
        assert outputs[2] == "\x1b[41m\x1b[37mError message\x1b[0m"
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        content = output.read().strip()
        assert content == "\x1b[47m\x1b[30mFile test\x1b[0m"
        output.close()