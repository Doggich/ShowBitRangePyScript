
# ------------------------------  Once a year, and the stick shoots     [ UwU ]
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ------------------------------

from modules.detail import ascii_format
from modules.parserBuilder import buildArgParser
from modules.showBitRange import showBitRangeForSignedInt, showBitRangeForUnsignedInt 

def main() -> None:
    """Main program function."""
    parser = buildArgParser()
    args = parser.parse_args() 
    int_type = args.int_type 
    number = args.number
    
    try:
        if int_type == "signed":
            description, (min_val, max_val) = showBitRangeForSignedInt(number)
        else:
            description, (min_val, max_val) = showBitRangeForUnsignedInt(number)
        
        # Using the format argument
        if args.format == "simple":
            print(f"Range for {ascii_format(int_type, 'bold', 'italic', 'underline')} integer with {ascii_format(str(number), 'bold', 'italic', 'underline')} bits:")
            print(f"Minimum value: {ascii_format(str(min_val), 'bold', 'italic', 'green')}")
            print(f"Maximum value: {ascii_format(str(max_val), 'bold', 'italic', 'green')}")
        elif args.format == "detailed":
            total_values = max_val - min_val + 1
            bin_min_value = f"{min_val:b}"
            bin_max_value = f"{max_val:b}"
            print(f"{ascii_format(int_type.upper(), 'bold', 'italic', 'underline')} {ascii_format(str(number), 'bold', 'italic', 'underline')}-bit Integer")
            print(f"Formula: {ascii_format(description, 'bold', 'italic', 'magenta')}")
            print(f"Range: {ascii_format(str(min_val), 'bold', 'italic', 'green')} to {ascii_format(str(max_val), 'bold', 'italic', 'green')}")
            print(f"Total values: {ascii_format(str(total_values), 'bold', 'italic', 'blue')}")
            print(f"Binary: {ascii_format(bin_min_value, 'bold', 'italic', 'yellow')} to {ascii_format(bin_max_value, 'bold', 'italic', 'yellow')}")
        elif args.format == "math":
            print(ascii_format(description, 'bold', 'italic', 'magenta'))
        elif args.format == "range":
            print(f"{ascii_format(str(min_val), 'bold', 'italic', 'green')} {ascii_format(str(max_val), 'bold', 'italic', 'green')}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
