# Number Prettifier

This project implements a **Number Prettifier** that converts large numbers into a human-readable, abbreviated format (e.g., 1M for 1,000,000). The implementation uses the **Strategy Pattern** to allow easy extension if new prettification rules are needed in the future. 

## Table of Contents

- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Design Overview](#design-overview)
- [Usage](#usage)
- [Testing](#testing)

## Problem Statement

### Problem
Write a number prettifier:

_Write tested code (in any language) that accepts a numeric type and returns a truncated, **"prettified"** string version. The prettified version should include one number after the decimal when the truncated number is not an integer. It should prettify numbers greater than 6 digits and support millions, billions and trillions._

### Assumptions

- **Input Type**: The input will be a ***non-negative*** numeric type (integer or float).
- **Output Format**: The output will be a string, representing the prettified version of the number.
- **Range**: The function will support numbers upto trillions. For numbers below a million, the function will return the number as-is.
- **Precision**: If the truncated number is not an integer, it will include one digit after the decimal point.

## Project Structure

```plaintext
number_prettifier/
├── prettifier/
│   ├── __init__.py        # Makes the directory a Python module
│   ├── prettifier.py      # Contains all the NumberPrettifier classes
│   └── strategies.py      # Contains all the strategies for number prettification
└── tests/
    └── test_large_number_prettifier.py # Contains unit tests for the LargeNumberPrettifier class
```

## Design Overview

### Strategy Pattern

The **Strategy Pattern** is used to define a family of algorithms (prettification strategies), encapsulate each one, and make them interchangeable. This pattern is suitable here because it allows for easy extension and modification of prettification rules without affecting the core logic.

### Components

- **PrettifyStrategy**: An abstract base class that defines the interface for prettification strategies.
- **DefaultPrettifyStrategy**: The default implementation that handles suffixes for millions, billions, and trillions.
- **LargeNumberPrettifier**: The class that uses a `PrettifyStrategy` to prettify numbers.

## Usage

### Prettifier Class

The `LargeNumberPrettifier` class is initialized with a prettification strategy (default is `DefaultPrettifyStrategy`). The `prettify` method can be called to convert numbers into their prettified format.

```python
from prettifier import LargeNumberPrettifier

# Create a LargeNumberPrettifier instance
prettifier = LargeNumberPrettifier()

# Prettify a number
result = prettifier.prettify(2500000.34)
print(result)  # Output: 2.5M
```

### Custom Strategies

You can create custom strategies by extending the `PrettifyStrategy` class.

> **Note:** Recommended approach is to add new strategies inside the **strategies.py** file within the prettifier module.


```python 
# strategies.py (Preferred)
class CustomPrettifyStrategy(PrettifyStrategy):
    def prettify(self, number: float) -> str:
        # Custom logic here
        pass
```

> **Alternate:** You can also extend `PrettfyStrategy` outside the module to define custom strategies.

```python 
# custom_strategy.py
from prettifier import PrettifyStrategy

class CustomPrettifyStrategy(PrettifyStrategy):
    def prettify(self, number: float) -> str:
        # Custom logic here
        pass
```

## Testing

Unit tests are provided in the `tests/test_prettifier.py` file. The tests cover a range of cases, including edge cases.

### Running Tests

You can run the tests using the following command from the project root folder:

```bash
python -m unittest tests/test_prettifier.py
```

