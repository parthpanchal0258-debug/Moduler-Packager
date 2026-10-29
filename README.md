# Multi-Utility Toolkit

A beginner-friendly Python project that combines useful tools for date and time operations, mathematical calculations, random data generation, UUID creation, file handling, and module exploration.

## Features

### 1. Datetime and Time Operations
- Display the current date and time.
- Calculate the difference between two dates.
- Format the current date using a custom format.
- Use a simple stopwatch.
- Run a countdown timer.

### 2. Mathematical Operations
- Calculate the factorial of a number.
- Calculate compound interest.
- Find sine, cosine, and tangent values.
- Calculate the area of a circle, rectangle, or triangle.

### 3. Random Data Generation
- Generate a random number.
- Generate a list of random numbers.
- Generate a random password.
- Generate a six-digit OTP.

### 4. Unique Identifier Generation
- Generate a UUID using Python's `uuid` module.

### 5. File Operations
- Create a new text file.
- Write data to a file.
- Read file contents.
- Append data to a file.

### 6. Module Attribute Exploration
- Explore available attributes of supported Python modules using `dir()`.

## Requirements

- Python 3.8 or newer recommended.
- No third-party packages are required.

## How to Run

1. Install Python if it is not already installed.
2. Save the program as `main.py`.
3. Open a terminal in the folder containing `main.py`.
4. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## How to Use

When the program starts, choose an option from the main menu by entering its number. Follow the prompts shown in the terminal. Select **7. Exit** to close the program.

## Project Structure

```text
Multi-Utility-Toolkit/
└── main.py
```

This README describes the single-file version of the project.

## Python Modules Used

- `datetime` — date and time handling.
- `time` — stopwatch timing and countdown delays.
- `math` — factorial, trigonometry, and geometric calculations.
- `random` — random numbers, lists, passwords, and OTP generation.
- `string` — character sets for password and OTP generation.
- `uuid` — unique identifier generation.
- `os` — included for standard-library module exploration.

## Notes

- File operations work with paths available to the program. Be careful when choosing a filename because writing with mode `w` replaces existing file contents.
- The random password and OTP features are intended for practice and demonstration, not for high-security production use.
- Invalid menu choices are handled with an error message.

## Future Improvements

- Split the program into separate modules and a package.
- Save operation logs to a file.
- Add more geometric shapes and mathematical utilities.
- Improve input validation and use `secrets` for security-sensitive passwords and OTPs.

## License

This project is for learning and educational use. Add a license if you plan to distribute it publicly.
