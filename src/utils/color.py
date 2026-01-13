from typing import Final, Tuple, Union

class FG:
    """ANSI escape codes for foreground (text) colors."""
    
    BLACK: Final[str] = "\033[30m"
    RED: Final[str] = "\033[31m"
    GREEN: Final[str] = "\033[32m"
    YELLOW: Final[str] = "\033[33m"
    BLUE: Final[str] = "\033[34m"
    MAGENTA: Final[str] = "\033[35m"
    CYAN: Final[str] = "\033[36m"
    WHITE: Final[str] = "\033[37m"
    GRAY: Final[str] = "\033[90m"
    BRIGHT_RED: Final[str] = "\033[91m"
    BRIGHT_GREEN: Final[str] = "\033[92m"
    BRIGHT_YELLOW: Final[str] = "\033[93m"
    BRIGHT_BLUE: Final[str] = "\033[94m"
    BRIGHT_MAGENTA: Final[str] = "\033[95m"
    BRIGHT_CYAN: Final[str] = "\033[96m"


class BG:
    """ANSI escape codes for background colors."""
    
    BLACK: Final[str] = "\033[40m"
    RED: Final[str] = "\033[41m"
    GREEN: Final[str] = "\033[42m"
    YELLOW: Final[str] = "\033[43m"
    BLUE: Final[str] = "\033[44m"
    MAGENTA: Final[str] = "\033[45m"
    CYAN: Final[str] = "\033[46m"
    WHITE: Final[str] = "\033[47m"
    GRAY: Final[str] = "\033[100m"
    BRIGHT_RED: Final[str] = "\033[101m"
    BRIGHT_GREEN: Final[str] = "\033[102m"
    BRIGHT_YELLOW: Final[str] = "\033[103m"
    BRIGHT_BLUE: Final[str] = "\033[104m"
    BRIGHT_MAGENTA: Final[str] = "\033[105m"
    BRIGHT_CYAN: Final[str] = "\033[106m"


class Style:
    """ANSI escape codes for text styles."""
    
    RESET: Final[str] = "\033[0m"
    BOLD: Final[str] = "\033[1m"
    DIM: Final[str] = "\033[2m"
    ITALIC: Final[str] = "\033[3m"
    UNDERLINE: Final[str] = "\033[4m"
    BLINK: Final[str] = "\033[5m"
    REVERSE: Final[str] = "\033[7m"
    HIDDEN: Final[str] = "\033[8m"
    STRIKETHROUGH: Final[str] = "\033[9m"
    DOUBLE_UNDERLINE: Final[str] = "\033[21m"

class Color:
    """ANSI color utilities with RGB support."""
    
    @staticmethod
    def _validate_rgb(r: int, g: int, b: int) -> None:
        """Validate RGB values are in range 0-255."""
        for name, value in [("Red", r), ("Green", g), ("Blue", b)]:
            if not 0 <= value <= 255:
                raise ValueError(f"{name} component must be between 0 and 255, got {value}")
    
    @classmethod
    def RGBFont(cls, *args: Union[int, Tuple[int, int, int]]) -> str:
        """Create ANSI escape code for RGB text color.
        
        Usage:
            Color.RGBFont(255, 0, 0)           # Red
            Color.RGBFont((255, 0, 0))         # Also red
            Color.RGBFont(255, g=0, b=0)       # Keyword args (Python 3.8+)
        
        Args:
            *args: Either three ints or a single tuple of three ints
        
        Returns:
            ANSI escape code for 24-bit RGB text color
        """
        if len(args) == 1 and isinstance(args[0], tuple):
            r, g, b = args[0]
        elif len(args) == 3:
            r, g, b = args
        else:
            raise ValueError("Expected either (r, g, b) or ((r, g, b),)")
        
        cls._validate_rgb(r, g, b)
        return f"\033[38;2;{r};{g};{b}m"
    
    @classmethod
    def RGBBack(cls, *args: Union[int, Tuple[int, int, int]]) -> str:
        """Create ANSI escape code for RGB background color.
        
        Usage:
            Color.RGBBack(255, 0, 0)           # Red
            Color.RGBBack((255, 0, 0))         # Also red
            Color.RGBBack(255, g=0, b=0)       # Keyword args (Python 3.8+)
        
        Args:
            *args: Either three ints or a single tuple of three ints
        
        Returns:
            ANSI escape code for 24-bit RGB text color
        """
        if len(args) == 1 and isinstance(args[0], tuple):
            r, g, b = args[0]
        elif len(args) == 3:
            r, g, b = args
        else:
            raise ValueError("Expected either (r, g, b) or ((r, g, b),)")
        
        cls._validate_rgb(r, g, b)
        return f"\033[48;2;{r};{g};{b}m"
    
    @staticmethod
    def invertRGB(r: int, g: int, b: int) -> Tuple[int, int, int]:
        """
        Invert an RGB color (complement in RGB color space).
        
        ### Args:
            r: Red (0-255)
            g: Green (0-255)
            b: Blue (0-255)
        
        ### Returns:
            Inverted color as (255-r, 255-g, 255-b)
        
        ### Example:
            Color.invertRGB(255, 0, 0)  # Returns (0, 255, 255) (red → cyan)
        """
        if not all(0 <= x <= 255 for x in (r, g, b)):
            raise ValueError("RGB values must be in range 0-255")
            
        return (255 - r, 255 - g, 255 - b)

