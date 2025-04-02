import io
import sys
import re
import pytest
from src.colored_logger import ColoredLogger

class TestColoredLogger:
    def test_default_log(self, capsys):
        """Test default logging behavior."""
        ColoredLogger.log("Test message")
        captured = capsys.readouterr()
        output = captured.out.strip()
        
        assert re.match(r'\x1b\[47m\x1b\[30mTest message\x1b\[0m', output)
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = {
            'red': '\x1b[41m', 'green': '\x1b[42m', 'yellow': '\x1b[43m', 
            'blue': '\x1b[44m', 'magenta': '\x1b[45m', 'cyan': '\x1b[46m', 
            'white': '\x1b[47m'
        }
        
        for color, color_code in colors.items():
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            output = captured.out.strip()
            
            assert re.match(f'{color_code}', output)
            assert 'Color test' in output
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\033[31m')
        captured = capsys.readouterr()
        output = captured.out.strip()
        
        assert re.match(r'\x1b\[47m\x1b\[31mTest\x1b\[0m', output)
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        outputs = captured.out.strip().split('\n')
        
        assert re.match(r'\x1b\[44m\x1b\[37mDebug message\x1b\[0m', outputs[0])
        assert re.match(r'\x1b\[43m\x1b\[30mWarning message\x1b\[0m', outputs[1])
        assert re.match(r'\x1b\[41m\x1b\[37mError message\x1b\[0m', outputs[2])
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        content = output.read().strip()
        assert re.match(r'\x1b\[47m\x1b\[30mFile test\x1b\[0m', content)
        output.close()