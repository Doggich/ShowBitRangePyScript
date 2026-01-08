import argparse

def buildArgParser() -> argparse.ArgumentParser:
    """
    Creates and configures a command line argument parser for the Bit Range Calculator.

    This function sets up the argument parser with three main arguments:
    - Integer type (signed or unsigned)
    - Output format (simple, detailed, math, or range)
    - Number of bits for calculation

    ### Returns:
        argparse.ArgumentParser: A configured argument parser ready to parse command line arguments.

    ### Arguments:
        -t, --int-type (required): Specifies the integer type to calculate range for.
            Choices: 'unsigned' or 'signed' (default: 'signed').
            - 'unsigned': For non-negative integers (0 and positive).
            - 'signed': For integers that can be positive, negative, or zero.

        -f, --format (optional): Controls the output format and verbosity.
            Choices: 'simple', 'detailed', 'math', 'range' (default: 'simple').
            - 'simple': Shows only the range (minimum and maximum values).
            - 'detailed': Shows formula, range, total values, and binary representation.
            - 'math': Shows only the mathematical formula for the range.
            - 'range': Shows only the numerical range values (space-separated).

        -n, --number (required): Specifies the number of bits for calculation.
            Must be a positive integer. For signed integers, minimum is 2 bits;
            for unsigned integers, minimum is 1 bit. Maximum supported is 1024 bits.

    ### Note:
        The bit number validation is performed after parsing by separate validation functions.
        This parser only ensures the argument types are correct.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Shows the range of numbers (unsigned/signed) for integers of the nth bit"
    )
    
    parser.add_argument("-t", "--int-type", 
                        type=str, 
                        dest="int_type", 
                        required=True, 
                        default="signed", 
                        choices=["unsigned", "signed"], 
                        help="choosing the type for an integer"
    )
    
    parser.add_argument("-f", "--format", 
                type=str,
                choices=["simple", "detailed", "math", "range"],
                default="simple",
                help="output format"
    )
    
    parser.add_argument("-n", "--number", 
                        type=int, 
                        dest="number",  
                        required=True,
                        help="the number whose range will be shown"
    )
    
    return parser