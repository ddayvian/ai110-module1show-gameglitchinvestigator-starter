# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
the game purpose was to play a random number guessing game, type in a random number and hope to get it, while you are given hints that cna indicate if your number is too high or too low. 
- [ ] Detail which bugs you found.
bugs i found was the secret hints given did not help at all in the direction of the secret number. as well as the difficulty ranges did not match the difficulty at all.
i also fixed the new game button not working.
- [ ] Explain what fixes you applied.
i fixed the new game button not working properly such as not reseting its history to let a new game start, fixed the hints actually helping in the direction of the secret number. i as well fixed the difficulty ranges.

## 📸 Demo

- [Fixed Game Screenshot] [winninggame.png]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
