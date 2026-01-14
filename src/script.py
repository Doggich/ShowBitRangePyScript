# ------------------------------  Once a year, and the stick shoots     [ UwU ]
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ------------------------------

from utils.format import ascii_format
from modules.argsParser import buildArgParser
from modules.showBitRange import ShowIntBitRange

def main() -> None:
    """
    Main entry point for the Bit Range Calculator application.

    ### This function orchestrates the entire program flow:
    1. Parses command-line arguments to get user input
    2. Calculates the integer range based on bit length and integer type
    3. Formats and displays the results using ANSI-colored output
    4. Handles errors and provides user-friendly error messages

    ### The program supports four output formats:
    - 'simple': Basic range information (minimum and maximum values)
    - 'detailed': Comprehensive information including formula, binary representation, and total values
    - 'math': Only the mathematical formula describing the range
    - 'range': Only the numerical range values (space-separated, useful for scripting)

    ### Workflow:
        1. Parse command-line arguments using buildArgParser()
        2. Validate input and calculate ranges using showBitRangeFor* functions
        3. Format output according to the specified format using ascii_format()
        4. Display results to the user

    ### Error Handling:
        - ValueError: Handles invalid bit counts or other input validation errors
        - Exception: Catches any unexpected errors and displays them gracefully

    ### Environment Requirements:
        - Terminal with ANSI color support for optimal display
        - Python 3.6 or higher (for f-string support)
        - Proper module structure with 'modules' directory

    ### Note:
        This function is designed to be called as the main entry point when
        the script is executed directly (via __name__ == "__main__").

    ### See Also:
        buildArgParser: For command-line argument parsing details
        showBitRangeForSignedInt: For signed integer range calculations
        showBitRangeForUnsignedInt: For unsigned integer range calculations
        ascii_format: For ANSI-colored text formatting
    """
    parser = buildArgParser()
    args = parser.parse_args() 
    int_type = args.int_type 
    number = args.number
    
    try:
        if int_type == "signed":
            temp: ShowIntBitRange = ShowIntBitRange(int_type='signed', bit=number)
            description, (min_val, max_val) = temp.get_info()
        else:
            temp: ShowIntBitRange = ShowIntBitRange(int_type='unsigned', bit=number)
            description, (min_val, max_val) = temp.get_info()
        
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
            print(f"Formula: {ascii_format(description, "formula")}")
            print(f"Range: {ascii_format(str(min_val), 'numeric_value')} to {ascii_format(str(max_val), 'numeric_value')}")
            print(f"Total values: {ascii_format(str(total_values), 'bold', 'italic', 'blue')}")
            print(f"Binary: {ascii_format(bin_min_value, 'binary_value')} to {ascii_format(bin_max_value, 'binary_value')}")
        elif args.format == "math":
            print(ascii_format(description, 'formula'))
        elif args.format == "range":
            print(f"{ascii_format(str(min_val), 'numeric_value')} {ascii_format(str(max_val), 'numeric_value')}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()