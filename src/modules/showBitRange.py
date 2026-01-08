from typing import Tuple
from .validatorForBit import validate_bit

def showBitRangeForSignedInt(bit: int) -> Tuple[str, Tuple[int, int]]:
    """
    Calculates and returns the numerical range for a signed integer of specified bit length.

    This function computes the minimum and maximum values that can be represented
    by a signed integer using two's complement representation for the given number of bits.
    It also returns a mathematical formula describing the range.

    ### Args:
        bit: The number of bits for the signed integer representation.
            Must be between 2 and 1024 (inclusive).

    ### Returns:
        Tuple[str, Tuple[int, int]]: A tuple containing:
            - str: Mathematical formula describing the range in human-readable format.
            - Tuple[int, int]: (minimum_value, maximum_value) that can be represented.

    ### Raises:
        ValueError: If the bit count is not between 2 and 1024.

    ### Notes:
        - For signed integers, one bit is reserved for the sign (positive/negative).
        - Uses two's complement representation which is standard for most modern systems.
        - The range is asymmetric: there is one more negative value than positive values.
        - Formula: [-2^(n-1), 2^(n-1)-1] where n is the number of bits.

    ### See Also:
        showBitRangeForUnsignedInt: For calculating ranges of unsigned integers.
        validate_bit: For input validation.
    """
    # For signed int, minimum 2 bits are required (1 for sign, 1 for value)
    validate_bit(bit=bit, min_bit=2, max_bit=1024)

    math_formula: str = f"[-2^{bit-1} to -1] ∪ [0 to 2^{bit-1} - 1]"
    min_number_from_range: int = -2**(bit-1)
    max_number_from_range: int = 2**(bit-1) - 1

    return (math_formula, (min_number_from_range, max_number_from_range))

def showBitRangeForUnsignedInt(bit: int) -> Tuple[str, Tuple[int, int]]:
    """
    Calculates and returns the numerical range for an unsigned integer of specified bit length.

    This function computes the minimum and maximum values that can be represented
    by an unsigned integer (non-negative only) for the given number of bits.
    It also returns a mathematical formula describing the range.

    ### Args:
        bit: The number of bits for the unsigned integer representation.
            Must be between 1 and 1024 (inclusive).

    ### Returns:
        Tuple[str, Tuple[int, int]]: A tuple containing:
            - str: Mathematical formula describing the range in human-readable format.
            - Tuple[int, int]: (minimum_value, maximum_value) that can be represented.

    ### Raises:
        ValueError: If the bit count is not between 1 and 1024.

    ### Notes:
        - Unsigned integers can only represent non-negative values (0 and positive).
        - All bits are used for representing magnitude (no sign bit).
        - The range is symmetric around zero starting from 0.
        - Formula: [0, 2^n - 1] where n is the number of bits.
        - With n bits, you can represent 2^n distinct values.

    ### See Also:
        showBitRangeForSignedInt: For calculating ranges of signed integers.
        validate_bit: For input validation.
    """
    # For unsigned int, 2 bit is sufficient
    validate_bit(bit=bit, min_bit=2, max_bit=1024)

    math_formula: str = f"[0 to 2^{bit} - 1]"
    min_number_from_range: int = 0 
    max_number_from_range: int = 2**bit - 1

    return (math_formula, (min_number_from_range, max_number_from_range))