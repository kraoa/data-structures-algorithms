Welcome to your practice interview. Use this session to familiarize yourself with the CoderPad environment that you will be using in your AI-Enabled SWE Coding interview. We've included a sample question, so that you have the option of experiencing the platform in a realistic way.

# The Puzzle

I’ve written a new game, and it works like this:

- Puzzle has a secret word.
- The player needs to guess the secret word, ideally in as few guesses as possible.
- When you guess a word via Puzzle.guess, you get information about each letter in your guess:
    - Match.YES if the secret word has that letter in that spot
    - Match.MOVE if that letter could be moved to be correct
    - Match.NO if the letter can’t be used
- If you can’t guess it, you can give up via Puzzle.admitDefeat to get the secret word.


# Your tasks

1. Explore the code. Figure out how the existing code works.
2. Press the green Run button to execute the code.
3. Use the dropdown arrow to select a different runnable. Run the unit tests. For some languages, look at the unit test file(s), and see that there are commented-out unit tests; uncomment them.
4. Fix the code to pass the unit tests. There might be bugs.
5. Implement the Solver to play the game and beat the puzzle.
6. Use the AI Assistant as much or as little as you would like.