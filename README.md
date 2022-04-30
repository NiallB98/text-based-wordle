# Text Based Wordle
A text-based version of the popular NY Times-owned game Wordle

## How to Play
The objective of the game is to guess a randomly selected 5-letter word within 6 guesses where each guess will reveal details about the word in question
- `Wrong` letters are denoted with `-` on either side:
\
| - A - |
\
Or in grey |<span style="background:#303030; color:white"> A </span>| with cmd line arg `--colours` (Shade of grey may differ)
- `Correct` letters in the `wrong position` are denoted with `()`:
\
| ( B ) |
\
Or in yellow |<span style="background:yellow; color:black"> B </span>| with cmd line arg `--colours`
- `Correct` letters in the `correct position` are denoted with `*` on either side:
\
| * C * |
\
Or in green |<span style="background:green; color:black"> C </span>| with cmd line arg `--colours`

## Commands
In-game it is possible to view a list of the game's commands by entering the `\help` command

## Command line arguments
`--colours` - Activates coloured mode

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