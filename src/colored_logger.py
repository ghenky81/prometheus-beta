import sys
import os

class ColoredLogger:
    """
    A utility class for logging messages with background colors.
    
    Supports different log levels and background colors for enhanced visibility.
    """
    
    # ANSI color codes for background colors
    COLORS = {
        'red': '\x1b[41m',
        'green': '\x1b[42m', 
        'yellow': '\x1b[43m',
        'blue': '\x1b[44m',
        'magenta': '\x1b[45m',
        'cyan': '\x1b[46m',
        'white': '\x1b[47m',
        'reset': '\x1b[0m'
    }
    
    @classmethod
    def log(cls, message, background_color='white', text_color=None, file=sys.stdout):
        """
        Log a message with a specified background color.
        
        Args:
            message (str): The message to log
            background_color (str, optional): Background color for the message. 
                Defaults to 'white'. 
                Options: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
            text_color (str, optional): Text color. Defaults to None (auto-selected).
            file (file object, optional): Output stream. Defaults to sys.stdout.
        
        Raises:
            ValueError: If an invalid background color is provided
        """
        # Validate background color
        if background_color not in cls.COLORS:
            raise ValueError(f"Invalid background color. Choose from {list(cls.COLORS.keys())}")
        
        # Determine text color for readability
        if text_color is None:
            # Default text color for light backgrounds
            light_backgrounds = ['white', 'yellow', 'cyan']
            text_color = '\x1b[30m' if background_color in light_backgrounds else '\x1b[37m'
        
        # Construct the colored log message
        colored_message = f"{cls.COLORS[background_color]}{text_color}{message}{cls.COLORS['reset']}"
        
        # Print the message
        print(colored_message, file=file, flush=True)
        
    @classmethod
    def debug(cls, message, **kwargs):
        """Log a debug message with blue background."""
        kwargs['background_color'] = 'blue'
        cls.log(message, **kwargs)
        
    @classmethod
    def warning(cls, message, **kwargs):
        """Log a warning message with yellow background."""
        kwargs['background_color'] = 'yellow'
        cls.log(message, **kwargs)
        
    @classmethod
    def error(cls, message, **kwargs):
        """Log an error message with red background."""
        kwargs['background_color'] = 'red'
        cls.log(message, **kwargs)