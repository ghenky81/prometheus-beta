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
    
    def test_background_colors(self, capsys):
        """Test all background colors."""
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        for color in colors:
            ColoredLogger.log("Color test", background_color=color)
            captured = capsys.readouterr()
            assert "Color test" in captured.out
    
    def test_invalid_background_color(self):
        """Test that invalid background colors raise ValueError."""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Test", background_color="invalid")
    
    def test_custom_text_color(self, capsys):
        """Test custom text color."""
        ColoredLogger.log("Test", background_color='white', text_color='\033[31m')
        captured = capsys.readouterr()
        assert "Test" in captured.out
    
    def test_log_methods(self, capsys):
        """Test special log methods."""
        ColoredLogger.debug("Debug message")
        ColoredLogger.warning("Warning message")
        ColoredLogger.error("Error message")
        
        captured = capsys.readouterr()
        assert "Debug message" in captured.out
        assert "Warning message" in captured.out
        assert "Error message" in captured.out
    
    def test_log_to_file(self):
        """Test logging to a file-like object."""
        # Create a string buffer to capture output
        output = io.StringIO()
        ColoredLogger.log("File test", file=output)
        output.seek(0)
        
        assert "File test" in output.read()
        output.close()