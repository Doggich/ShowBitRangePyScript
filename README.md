# Bit Range Calculator

A Python command-line tool for calculating the numeric ranges of signed and unsigned integers based on bit length with beautiful ANSI-colored output.

---

## 📋 Features

* Bit Range Calculation: Calculate min/max values for signed and unsigned integers
* Multiple Output Formats: Simple, detailed, mathematical formula, and range-only formats
* ANSI Color Support: Beautiful colored terminal output with customizable styles
* Input Validation: Validates bit length constraints
* Modular Architecture: Clean separation of concerns for easy maintenance

---

## 📊 Supported Bit Ranges

* Signed integers: 2 to 1024 bits
* Unsigned integers: 2 to 1024 bits

---

## 🚀 Installation

## Prerequisites

* `Python 3.6` or higher
* Terminal with `ANSI` color support (most modern terminals)

## Manual Installation

1. Clone or download the project:
   
```bash
git clone <repository-url>
cd python_scripts
```

2. The tool is ready to use - no external dependencies required!

---

## 💻 Usage

### Basic Syntax

```bash
python script.py --int-type <type> --number <bits> [--format <format>]
```

## Required Arguments

* `--int-type` (`-t`): Integer type - `signed` or `unsigned`
* `--number` (`-n`): Bit length (1-1024 for `unsigned`, 2-1024 for signed)

## Optional Arguments

`--format` (`-f`): Output format - `simple`, `detailed`, `math`, or `range` (default: simple)

## Examples

1. Basic signed integer range:

```bash
python script.py --int-type signed --number 8
```

*Outputs the range of an 8-bit signed integer*

2. Detailed unsigned integer information:

```bash
python script.py --int-type unsigned --number 16 --format detailed
```

*Shows comprehensive information including binary representation*

3. Mathematical formula only:

```bash
python script.py --int-type signed --number 32 --format math
```

*Displays only the mathematical formula for the range*

4. Range values only (for scripting):

```bash
python script.py --int-type unsigned --number 64 --format range
```

*Outputs only the min and max values (useful for scripts)*

---

## 🎨 Output Formats

1. ## Simple Format (Default)

Displays the range in a clean, readable format with colored highlights.

2. ## Detailed Format

Provides comprehensive information including:

* Integer type and bit length
* Mathematical formula
* Numeric range
* Total number of representable values
* Binary representation range

3. ## Math Format

Shows only the mathematical formula describing the range.

4. ## Range Format

Outputs only the minimum and maximum values (space-separated), useful for scripting.

## 📁 Project Structure

```text
src/
├── script.py                   - # Main entry point
└── modules/                    - # Core modules
    ├── __init__.py            -- # Package initialization
    ├── detail.py              -- # ANSI color formatting utilities
    ├── parserBuilder.py       -- # CLI argument parser builder
    ├── showBitRange.py        -- # Core range calculation logic
    └── validatorForBit.py     -- # Input validation functions
```

## Module Descriptions

* `detail.py`: Handles ANSI escape codes for colored and styled terminal output
* `parserBuilder.py`: Configures command-line argument parsing
* `showBitRange.py`: Contains the mathematical logic for calculating integer ranges
* `validatorForBit.py`: Validates input parameters (bit length constraints)

---

## 🤝 Contributing

* Fork the repository
* Create a feature branch (`git checkout -b feature/amazing-feature`)
* Commit your changes (`git commit -m "Add amazing feature"`)
* Push to the branch (`git push origin feature/amazing-feature`)
* Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

[Doggich](https://github.com/Doggich)  - Initial work

