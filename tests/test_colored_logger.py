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
        assert output.endswith("Test message\x1b[0m")
        assert output.startswith("\x1b[47m\x1b[30m")
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        for color in colors:
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            output = captured.out.strip()
            assert output.endswith("Color test\x1b[0m")
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\033[31m')
        captured = capsys.readouterr()
        output = captured.out.strip()
        assert output.endswith("Test\x1b[0m")
        assert output.startswith("\x1b[47m\x1b[31m")
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        outputs = captured.out.strip().split('\n')
        
        assert outputs[0].endswith("Debug message\x1b[0m")
        assert outputs[0].startswith("\x1b[44m\x1b[37m")
        
        assert outputs[1].endswith("Warning message\x1b[0m")
        assert outputs[1].startswith("\x1b[43m\x1b[30m")
        
        assert outputs[2].endswith("Error message\x1b[0m")
        assert outputs[2].startswith("\x1b[41m\x1b[37m")
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        content = output.read()
        assert "File test" in content
        output.close()