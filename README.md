# Number2french 

## Introduction
This Python package provides a command-line tool to convert numbers into their word representation in either French or Belgian. It can handle individual numbers or lists of numbers from a JSON file.

## Installation

1. Clone the repository

2. Navigate to the repository directory

3. Install the package:
   ```
   pip install .
   ```

## Usage

The tool can be used in two modes: converting a single number or converting a list of numbers from a file.

### Converting a Single Number

To convert a single number, use the `-n` or `--number` option followed by the number. Specify the language using `-l` or `--language` (`french` or `belgian`):

```
number2french -n 42 -l french
```

### Converting Numbers from a File

To convert numbers from a JSON file, use the `-f` or `--file` option followed by the file path. Optionally, output can be saved to a file using the `-o` or `--output` option:

```
number2french -f path/to/numbers.json -l belgian -o path/to/output.json
```

The JSON file should have the numbers stored under a key named 'numbers', like so:

```json
{
  "numbers": [1, 2, 3, 42]
}
```

### Output

The output will be displayed on the command line or saved to the specified output file in JSON format.
