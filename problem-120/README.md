Welcome to your practice interview. Use this session to familiarize yourself with the CoderPad environment that you will be using in your AI-Enabled SWE Coding interview. We've included a sample question, so that you have the option of experiencing the platform in a realistic way.

# Minesweeper

You are given a minesweeper board and a click position. Implement the reveal mechanic:

- Each cell is one of: `'M'` (unrevealed mine), `'E'` (unrevealed empty), `'B'` (revealed blank), `'X'` (revealed mine), or `'1'`–`'8'` (revealed with adjacent mine count).
- If the clicked cell is a mine `'M'`, change it to `'X'` (game over).
- If the clicked cell is empty `'E'`:
    - Count its 8-directional adjacent mines.
    - If the count is > 0, change the cell to that digit and stop.
    - If the count is 0, change the cell to `'B'` and recursively reveal all adjacent `'E'` cells.
- Return the updated board.

# Your tasks

1. Explore the code. Figure out how the existing code works.
2. Press the green Run button to execute the code.
3. Use the dropdown arrow to select a different runnable. Run the unit tests. For some languages, look at the unit test file(s), and see that there are commented-out unit tests; uncomment them.
4. Fix the code to pass the unit tests. There might be bugs.
5. Implement the Solver.
6. Use the AI Assistant as much or as little as you would like.
