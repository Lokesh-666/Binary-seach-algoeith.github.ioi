# Binary Search Program

This is a simple binary search program implemented in Python. It allows the user to search for an element in a sorted list using the binary search algorithm.

## Features

- Performs binary search on a sorted list.
- Returns the position of the target element if found.
- Provides feedback on whether the element was found or not.

## Requirements

To run this program, you need to have Python installed on your system.

## Installation

1. **Install Python:**

   Make sure you have Python installed. You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

   To check if Python is already installed, you can run the following command in your terminal or command prompt:

   ```sh
   python --version
   ```

   or

   ```sh
   python3 --version
   ```

2. **Download the Code:**

   Clone or download this repository to your local machine.

   ```sh
   git clone https://github.com/yourusername/binary-search.git
   ```

   Navigate to the directory where you have saved the code.

   ```sh
   cd binary-search
   ```

## How to Run the Program

1. Open your terminal or command prompt.
2. Navigate to the directory where the code is saved.
3. Run the following command to start the program:

   ```sh
   python binary_search.py
   ```

   or

   ```sh
   python3 binary_search.py
   ```

## Usage

1. The program contains a predefined list of sorted elements.
2. The target element to search for is also predefined in the code.
3. The binary search function will search for the target element in the list.
4. The program will output the position of the target element if found, or indicate that the value was not found.

## Example

The following example demonstrates the output of the program when searching for the element `121` in the list:

```python
list = [45, 56, 86, 98, 99, 100, 121, 134, 154]
result = binary_search(list, 121)
verify(result)
```

Output:

```
Target found at position: 8
```

## Notes

- The list must be sorted for the binary search algorithm to work correctly.
- The position returned is based on a 1-based index for user-friendly output, but internally the program uses a 0-based index.

## Contributing

If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License.
