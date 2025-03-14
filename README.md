# Typingsterm

A simple terminal-based typing speed test application written in Python. This program uses the `curses` library to display a randomized text sample and provides real-time, colored feedback as you type. Once you complete the test by typing the last character of the text, your typing speed in words per minute (WPM) is calculated and displayed. After viewing your results, you can press Enter to start a new test or Escape to exit.

## Features

- **Randomized Text:** Generates a random text sample from a predefined list of common English words.
- **Real-Time Feedback:** Colors each character as you type:
  - **Green:** Correctly typed characters.
  - **Red:** Incorrectly typed characters.
  - **Cyan:** Characters not yet typed.
- **Automatic Test Completion:** Ends the test automatically when the last character is typed.
- **Results Display:** Shows elapsed time and calculates your typing speed (WPM).
- **Multiple Tests:** After finishing a test, press Enter to start another test or Escape to quit.

## Installation

1. Clone the Repository:

```bash
git clone https://github.com/gripebomb/typingsterm.git
cd typingsterm
```

2. Ensure You Have Python 3 Installed:  This program requires Python 3.x.

3. (For Windows Users) Install the windows-curses Package:
Windows does not include the curses module by default. Install it via pip:

```bash
pip install windows-curses
```

### Usage

Run the program in your terminal:

```bash
python typingsterm.py
```

### How It Works

- Start the Test:

    When you run the program, you'll see a random text sample along with instructions.

- During the Test:

    Type the text shown. The program gives immediate visual feedback by changing the color of each character as you type.

- Completing the Test:

    The test automatically finishes when you type the final character of the text. Your results, including elapsed time and WPM, are then displayed.

- Starting a New Test or Exiting:
    After the test, press Enter to start a new test or press Escape to quit the program.

### Dependencies

- Python 3.x
- curses (built-in on Unix-based systems)
- windows-curses (for Windows, install via pip)

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
License

This project is licensed under the MIT License.
