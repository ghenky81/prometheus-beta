import sys

class ColoredLogger:
    """
    A utility class for logging messages with background colors.
    
    Supports different log levels and background colors for enhanced visibility.
    """
    
    # ANSI color codes for background colors
    COLORS = {
        'red': '\033[41m',
        'green': '\033[42m', 
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'reset': '\033[0m'
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
            text_color = '\033[30m' if background_color in light_backgrounds else '\033[37m'
        
        # Construct the colored log message
        colored_message = f"{cls.COLORS[background_color]}{text_color}{message}{cls.COLORS['reset']}"
        
        # Print the message
        print(colored_message, file=file)
        
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