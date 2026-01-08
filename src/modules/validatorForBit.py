def validate_bit(bit: int, min_bit: int = 1, max_bit: int = 1024) -> None:
    """Checks if the bit count is within the valid range."""
    if not (min_bit <= bit <= max_bit):
        raise ValueError(f"Bit count must be between {min_bit} and {max_bit}")