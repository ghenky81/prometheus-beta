import io
import sys
import pytest
from src.colored_logger import ColoredLogger

class TestColoredLogger:
    def test_default_log(self, capsys):
        """Test default logging behavior."""
        ColoredLogger.log("Test message")
        captured = capsys.readouterr()
        # Check for the ANSI color codes and the message
        assert "\x1b[47m\x1b[30mTest message\x1b[0m" in captured.out
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        for color in colors:
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            # Verify ANSI color code and message
            assert f"\x1b[4{colors.index(color)+1}m" in captured.out
            assert "Color test" in captured.out
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\033[31m')
        captured = capsys.readouterr()
        assert "\x1b[47m\x1b[31mTest\x1b[0m" in captured.out
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        assert "\x1b[44m\x1b[37mDebug message\x1b[0m" in captured.out
        assert "\x1b[43m\x1b[30mWarning message\x1b[0m" in captured.out
        assert "\x1b[41m\x1b[37mError message\x1b[0m" in captured.out
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        assert "File test" in output.read()
        output.close()