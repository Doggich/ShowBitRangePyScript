from typing import Tuple
from .validatorForBit import validate_bit

def showBitRangeForSignedInt(bit: int) -> Tuple[str, Tuple[int, int]]:
    """Returns the range for a signed integer of the specified bit length."""
    # For signed int, minimum 2 bits are required (1 for sign, 1 for value)
    validate_bit(bit=bit, min_bit=2, max_bit=1024)

    math_formula: str = f"[-2^{bit-1} to -1] ∪ [0 to 2^{bit-1} - 1]"
    min_number_from_range: int = -2**(bit-1)
    max_number_from_range: int = 2**(bit-1) - 1

    return (math_formula, (min_number_from_range, max_number_from_range))

def showBitRangeForUnsignedInt(bit: int) -> Tuple[str, Tuple[int, int]]:
    """Returns the range for an unsigned integer of the specified bit length."""
    # For unsigned int, 1 bit is sufficient
    validate_bit(bit=bit, min_bit=2, max_bit=1024)

    math_formula: str = f"[0 to 2^{bit} - 1]"
    min_number_from_range: int = 0 
    max_number_from_range: int = 2**bit - 1

    return (math_formula, (min_number_from_range, max_number_from_range))