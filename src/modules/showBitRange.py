from typing import Tuple

class ShowIntBitRange():
    def __init__(self, int_type: str, bit: int) -> None:
        self.int_type = int_type
        self.bit = bit

    def __validate_bit(self, bit_: int, min_bit: int = 1, max_bit: int = 1024) -> None:
        if not (min_bit <= bit_ <= max_bit):
            raise ValueError(f"Bit count must be between {min_bit} and {max_bit}")
        
    def get_info(self) -> Tuple[str, Tuple[int, int]]:
        match self.int_type:
            case "signed":

                self.__validate_bit (bit_=self.bit, min_bit=2, max_bit=1024)

                math_formula: str = f"[-2^{self.bit-1} to -1] ∪ [0 to 2^{self.bit-1} - 1]"
                min_number_from_range: int = -2**(self.bit-1)
                max_number_from_range: int = 2**(self.bit-1) - 1

                return (math_formula, (min_number_from_range, max_number_from_range))
            
            case "unsigned":

                self.__validate_bit (bit_=self.bit, min_bit=2, max_bit=1024)

                math_formula: str = f"[0 to 2^{self.bit} - 1]"
                min_number_from_range: int = 0 
                max_number_from_range: int = 2**self.bit - 1

                return (math_formula, (min_number_from_range, max_number_from_range))                
    
