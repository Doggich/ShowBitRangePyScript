from utils.color import FG, BG, Style

def ascii_format(text: str, *styles: str) -> str:
    """
    Apply ANSI styles to text.

    ### Available styles:
        - "bold": Bold text
        - "italic": Italic (cursive) text
        - "underline": Underlined text
        - "strike": Strikethrough text
        - "red": Red text color
        - "green": Green text color
        - "blue": Blue text color
        - "yellow": Yellow text color
        - "magenta": Magenta text color
        - "cyan": Cyan text color
        - "black": Black text color
        - "white": White text color

    You can combine multiple styles (e.g., "bold", "italic", "red").

    ### Args:
        text: The text to format.
        *styles: One or more style names (see above).

    ### Returns:
        The formatted text with ANSI escape codes.
    """
    style_codes = {
        "bold": Style.BOLD,
        "italic": Style.ITALIC,
        "underline": Style.UNDERLINE,
        "strike": Style.STRIKETHROUGH,
        "red": FG.RED,
        "green": FG.GREEN,
        "blue": FG.BLUE,
        "yellow": FG.YELLOW,
        "magenta": FG.MAGENTA,
        "cyan": FG.CYAN,
        "black": FG.BLACK,
        "white": FG.WHITE,
        "formula": Style.BOLD + Style.ITALIC + FG.MAGENTA,
        "numeric_value": Style.BOLD + Style.ITALIC + FG.GREEN,
        "binary_value": Style.BOLD + Style.ITALIC + FG.YELLOW,
        "total": Style.BOLD + Style.ITALIC + FG.BLUE,

    }
    
    tags = "".join(style_codes.get(style, "") for style in styles)
    return f"{tags}{text}\033[0m"
        
