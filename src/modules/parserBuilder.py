import argparse

def buildArgParser() -> argparse.ArgumentParser:
    """Creates a command line argument parser."""
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