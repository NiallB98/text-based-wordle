# Text Based Wordle
A text-based version of the popular NY Times-owned game Wordle

## How to Play
The objective of the game is to guess a randomly selected 5-letter word within 6 guesses where each guess will reveal details about the word in question
- `Wrong` letters are denoted with `-` on either side:
\
| - A - |
\
Or coloured with a black/grey background in coloured mode (See [Commands](#commands) or [Command line arguments](#command-line-arguments))
- `Correct` letters in the `wrong position` are denoted with `()`:
\
| ( B ) |
\
Or coloured with a yellow background in coloured mode
- `Correct` letters in the `correct position` are denoted with `*` on either side:
\
| * C * |
\
Or coloured with a green background in coloured mode

## Commands
- `\help`
  - View the list of in-game commands
- `\q`
  - Quits the game
- `\r`
  - Restarts the game
- `\colours`
  - Toggles coloured mode
- `\debug`
  - Toggles debug mode

## Command line arguments
- `--debug`
  - Activates debug mode
- `--colours`
  - Activates coloured mode

\
**Note:** Coloured mode requires the `termcolor` module to be installed (`pip install termcolor`) if running via the source code

## Adding command line arguments for exe
If you wish to apply a command line argument to your exe easily:
- Create a shortcut to the exe
- Edit the properties of the shortcut
- Append the argument to the end of the `Target:` box
\
\
Your target box should look something like this:
`"C:\Path\To\Text Based Wordle.exe" --colours`
\
(If using the `--colours` argument for example)