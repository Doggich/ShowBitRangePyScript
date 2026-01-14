from typing import Tuple

class ShowIntBitRange():
    """
    A class to represent integer value ranges based on bit size and signedness.
    
    This class calculates the mathematical formula and actual value range
    for signed and unsigned integers of a given bit size.
    
    Attributes:
        int_type (str): Type of integer - "signed" or "unsigned"
        bit (int): Number of bits used for integer representation
    
    Raises:
        ValueError: If bit count is outside allowed range or unsupported integer type is provided
    
    Usage:
        >>> range_info = ShowIntBitRange("signed", 8)
        >>> formula, (min_val, max_val) = range_info.get_info()
        >>> print(f"Formula: {formula}")
        >>> print(f"Range: {min_val} to {max_val}")
        Formula: [-2^7 to -1] ∪ [0 to 2^7 - 1]
        Range: -128 to 127
    """
    
    def __init__(self, int_type: str, bit: int) -> None:
        """
        Initialize the integer bit range calculator.
        
        Args:
            int_type: Type of integer - "signed" (two's complement) or "unsigned"
            bit: Number of bits for integer representation (2-1024)
        """
        self.int_type = int_type
        self.bit = bit

    def __validate_bit(self, bit_: int, min_bit: int = 1, max_bit: int = 1024) -> None:
        """
        Validate that bit count is within allowed range.
        
        Args:
            bit_: Bit count to validate
            min_bit: Minimum allowed bit count
            max_bit: Maximum allowed bit count
        
        Raises:
            ValueError: If bit count is outside allowed range
        """
        if not (min_bit <= bit_ <= max_bit):
            raise ValueError(f"Bit count must be between {min_bit} and {max_bit}")
        
    def get_info(self) -> Tuple[str, Tuple[int, int]]:
        """
        Get mathematical formula and actual value range for the integer type and bit size.
        
        Returns:
            Tuple containing:
                - Mathematical formula string representing the range
                - Tuple of (minimum_value, maximum_value) for the range
        
        Raises:
            ValueError: If bit count is invalid for the given type
        """
        match self.int_type:
            case "signed":
                self.__validate_bit(bit_=self.bit, min_bit=2, max_bit=1024)

                math_formula: str = f"[-2^{self.bit-1} to -1] ∪ [0 to 2^{self.bit-1} - 1]"
                min_number_from_range: int = -2**(self.bit-1)
                max_number_from_range: int = 2**(self.bit-1) - 1

                return (math_formula, (min_number_from_range, max_number_from_range))
            
            case "unsigned":
                self.__validate_bit(bit_=self.bit, min_bit=2, max_bit=1024)

                math_formula: str = f"[0 to 2^{self.bit} - 1]"
                min_number_from_range: int = 0 
                max_number_from_range: int = 2**self.bit - 1

                return (math_formula, (min_number_from_range, max_number_from_range))