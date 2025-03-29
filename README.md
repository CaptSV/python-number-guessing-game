# Python Number Guessing Game

A simple command-line game where the user tries to guess a randomly generated number between 1 and 20 within a limited number of attempts.

## Description

This Python script provides a fun and interactive number guessing game. The program generates a secret random integer between 1 and 20, and the player has three attempts to guess the correct number. After each incorrect guess, the program provides feedback indicating whether the guess was too high or too low. If the player fails to guess the number within the allowed tries, the correct answer is revealed. The game then prompts the player if they want to try again.

## Getting Started

### Dependencies

* **Python 3:** This program is written in Python 3 and requires a Python 3 interpreter to be installed on your system. It utilizes the built-in `random` module. No additional libraries need to be installed via pip.
* **Operating System:** This program is designed to run on any operating system where Python 3 is supported.

### Installing

1.  **Download the script:** Save the Python code for the number guessing game into a file named `guessing_game.py` on your local machine. You can create this file using any text editor or integrated development environment (IDE) like PyCharm.
2.  **No specific installation steps are required.** This is a standalone Python script that can be executed directly. Ensure the file has the `.py` extension.

### Executing program

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** where you saved the `guessing_game.py` file using the `cd` command.
    ```bash
    cd path/to/your/script/directory
    ```
    (Replace `path/to/your/script/directory` with the actual path.)
3.  **Run the program** by executing the Python interpreter on the script:
    ```bash
    python guessing_game.py
    ```
4.  **Follow the on-screen prompts** to play the game. You will be asked to enter your guess, and the program will provide feedback.
5.  After each game (win or lose), you will be prompted if you want to try again by entering 'Y' for yes or 'N' for no.

## Development Roadmap

* **Improved Input Validation:** Implement more robust input validation to specifically provide feedback if the user enters non-numeric characters (e.g., symbols like "!", "%", etc.) instead of just indicating "Invalid input."
* **Difficulty Levels:** Introduce different difficulty levels that could affect the range of the random number or the number of allowed tries.
* **Score Tracking:** Keep track of the player's score across multiple games.
* **Screen Clearing (Cross-Platform):** Integrate screen clearing functionality in a way that works reliably across different operating systems.

## Help

* **Invalid Input:** If you enter a text value when prompted for a guess, the program will display an "Invalid Guess!" message and ask for a valid number.
* **Out of Range Guess:** If you enter a number that is less than 1 or greater than 20, the program will display "Invalid Guess!" and not count it as a try.

## Authors

Simon Valenzuela
[https://github.com/CaptSV](https://github.com/CaptSV)

## Version History

* 0.1
    * Initial release of the number guessing game with random number generation, user input, feedback (too high/low/correct), limited tries, and an option to play again.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

* This project was inspired by classic number guessing games.
* Utilizes Python's built-in `random` module.
