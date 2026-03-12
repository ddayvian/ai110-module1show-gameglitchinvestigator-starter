# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
  what was broken was that the ranges of difficulty did not match with its ranges. 
  the secret and the hint did not correlate with each other. 
  once you use all attempts, and click new game, a new game will not start.
- What did the game look like the first time you ran it?
  the game looked very confusing, it had wrong ui/ux problems, and already seemed buggy
- List at least two concrete bugs you noticed at the start  
  the difficulty range did not match with the range the game tells you to guess between.
  secret number and the hint did not match up with one another, they were not corelating.
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?
  how i used AI as a teammate was by asking it questions. i had asked it to break down tasks for me, automate code, fix bugges and even fix its own mistakes.
- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? i used copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
one example can be when i had asked it to fix the ranges for difficulty, in order for me to see if it was good results, luckily the code was very easy to fix, and was a simple error issue that was easy to fix so when seeing AI fixed it and give the correct ranges, verifying was no struggle. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
an ai suggestion that was incorrect for me was when the new game button it did not reset the history. which i had to check for and tell it to do. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
i decided wether a bug was really fixed by going back and testing the app again to see if working and by the pytest i created.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  a test i ran is a test that makes sure the hint works with the secret. what it showed me about my code is that it is working.
- Did AI help you design or understand any tests? How?
AI def helped me design and understand all my tests that was needed, by one asking it to create, two making sure it had explained back to me what was going on in the test.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Every time you clicked "Submit" or interacted with the app, Streamlit would rerun the entire script from top to bottom, which regenerated a new random number each time unless it was protected by session state.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns your code every time someone clicks a button or interacts with the app, like restarting a video game, but session state is like a memory box that survives each restart and remembers important variables between reruns.
- What change did you make that finally gave the game a stable secret number?
I wrapped the secret number generation in an `if "secret" not in st.session_state:` check so that the random number is only created once, and then remembered across all future reruns of the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
one habit id like to reuse is def pytest.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
next time what i would do differently is def setup better prompts. and use claude instead of copilot github
- In one or two sentences, describe how this project changed the way you think about AI generated code.
this proj changed the way i think by allowing me to see the errors of ai coding and that we as humans must double checked them as well. yes it can be helpful to have everything done for you but we are the cleaners, we must make sure what is written is clean and not messy.