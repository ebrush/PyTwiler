# PyTwiler
Python 3 interpreter, adaptable language implementation, future compiler, more. All in nearly-pure Python.

## Language Coverage
Currently supports simple expressions and assignments. Aims to support functions, classes, and other classic Python elements.

## Compatibility
Known to run with different versions of Python 3

## Setup
1. Have Python 3
2. Download project
3. Run `pip install pytest` if not installed already

## Running Tests
### Windows
Double-click "run_tests.bat"
### Other
Execute `python -m pytest` in project directory

## Modules
Evaluator - runs a series of tokens as code and returns a result

Preprocessor - changes parenthesized sequences of tokens into sublists, changes string tokens to appropriate datatype, etc

Tokenizer - returns from a file-like object a list of lists of strings matching the language's lexemes definitions

*_test.py - test for corresponding module to be picked up by pytest
