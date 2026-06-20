# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game seemed to run smoothly at first. The UI was clean and we could see what the correct answer was in the guessing game.
  This gave us a good reference point to begin debugging.

- List at least two concrete bugs you noticed at the start

  The hints kept telling us to go lower even when we were at zero, but higher when we were greater than the correct answer which doesnt make sense.
  
  The score does not reset to 0 when starting a new game. 
  
  The game also ignores the difficulty level on the left hand side.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input        | Expected Behavior        | Actual Behavior        | Console Output / Error |
|-------       |-------------------       |-----------------       |------------------------|
|5             |     too low              |      too low           | correct no error       |
| Easy Mode    |     value between 1-20   |      85                | Incorrect/erro         |
| game reset   |     reset attempts       |      attempts = 1      | incorrect/ error       |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  I used Claude to work on this

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI assistant notified me that the Too High or Too Low features were swapped. I went ahead and tested this out by
  purposefully using  a number that was lower than the answer. What the AI suggested is below:
  app.py:37-40	"Go HIGHER"/"Go LOWER" hints are swapped
  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI suggested that the game reset was flawed. This means that attemtps were never reset to their intended value.
  I tested this by playing a game and then resetting it (or clicking new game). Upon clicking new game, attempts were still at 1.
  This was rather hard to tease out as it was somewhat ambiguous.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
