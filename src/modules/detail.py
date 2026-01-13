class Text:
    class Font:
        Black = "\033[30m"
        Red = "\033[31m"
        Green = "\033[32m"
        Yellow = "\033[33m"
        Blue = "\033[34m"
        Magenta = "\033[35m"
        Cyan = "\033[36m"
        White = "\033[37m"
        Bright_black = "\033[90m"
        Bright_red = "\033[91m"
        Bright_green = "\033[92m"
        Bright_yellow = "\033[93m"
        Bright_blue = "\033[94m"
        Bright_magenta = "\033[95m"
        Bright_cyan = "\033[96m"

    class Back:
        Black = "\033[40m"
        Red = "\033[41m"
        Green = "\033[42m"
        Yellow = "\033[43m"
        Blue = "\033[44m"
        Magenta = "\033[45m"
        Cyan = "\033[46m"
        White = "\033[47m"
        Bright_black = "\033[100m"
        Bright_red = "\033[101m"
        Bright_green = "\033[102m"
        Bright_yellow = "\033[103m"
        Bright_blue = "\033[104m"
        Bright_magenta = "\033[105m"
        Bright_cyan = "\033[106m"

    class Tool:
        Flush = "\033[0m"
        Bold = "\033[1m"
        Cursive = "\033[3m"
        Underline = "\033[4m"
        Strike = "\033[9m"
        Dual_underline = "\033[21m"


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
        "bold": Text.Tool.Bold,
        "italic": Text.Tool.Cursive,
        "underline": Text.Tool.Underline,
        "strike": Text.Tool.Strike,
        "red": Text.Font.Red,
        "green": Text.Font.Green,
        "blue": Text.Font.Blue,
        "yellow": Text.Font.Yellow,
        "magenta": Text.Font.Magenta,
        "cyan": Text.Font.Cyan,
        "black": Text.Font.Black,
        "white": Text.Font.White,
        "formula": Text.Tool.Bold + Text.Tool.Cursive + Text.Font.Magenta,
        "numeric_value": Text.Tool.Bold + Text.Tool.Cursive + Text.Font.Green,
        "binary_value": Text.Tool.Bold + Text.Tool.Cursive + Text.Font.Yellow,
        "total": Text.Tool.Bold + Text.Tool.Cursive + Text.Font.Blue,

    }
    
    tags = "".join(style_codes.get(style, "") for style in styles)
    return f"{tags}{text}\033[0m"
        
