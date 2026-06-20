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
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Launch the app.** Run `python -m streamlit run app.py`. The browser opens to the Game Glitch Investigator. The sidebar shows **Normal** difficulty is selected by default, with a range of 1 to 100 and 8 attempts allowed.

2. **Start a new game.** The app has already picked a secret number. Open the **Developer Debug Info** expander to confirm — for this walkthrough, suppose the secret is **42**. The info banner reads: *"Guess a number between 1 and 100. Attempts left: 8."*

3. **First guess — too high.** Type `80` in the input box and click **Submit Guess 🚀**. The hint reads: *"📉 Go LOWER!"* Score drops by 5. Attempts left: 7.

4. **Second guess — too low.** Type `20` and submit. The hint reads: *"📈 Go HIGHER!"* Score drops by 5 again. Attempts left: 6.

5. **Third guess — closing in.** Type `50` and submit. Hint: *"📉 Go LOWER!"* Score drops by 5. Attempts left: 5.

6. **Fourth guess — one step away.** Type `40` and submit. Hint: *"📈 Go HIGHER!"* Score drops by 5. Attempts left: 4.

7. **Fifth guess — correct!** Type `42` and submit. Confetti balloons fill the screen and a success banner reads: *"🎉 You won! The secret was 42. Final score: 50."* The guess form is hidden and the game waits for a new game to be started.

8. **Start a new game.** Click **New Game 🔁**. Score, attempts, and history all reset. A new secret number is picked within the 1–100 range and the banner confirms: *"New game started."*

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.0.3, pluggy-1.6.0 -- c:\Users\gonza\OneDrive\Desktop\CodePath\Unit-1\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\gonza\OneDrive\Desktop\CodePath\Unit-1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 35 items

tests/test_game_logic.py::test_difficulty_easy PASSED                    [  2%]
tests/test_game_logic.py::test_difficulty_normal PASSED                  [  5%]
tests/test_game_logic.py::test_difficulty_hard_is_wider_than_normal PASSED [  8%]
tests/test_game_logic.py::test_difficulty_hard_range PASSED              [ 11%]
tests/test_game_logic.py::test_difficulty_unknown_returns_default PASSED [ 14%]
tests/test_game_logic.py::test_parse_guess_valid_integer PASSED          [ 17%]
tests/test_game_logic.py::test_parse_guess_decimal_rounds_to_int PASSED  [ 20%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED           [ 22%]
tests/test_game_logic.py::test_parse_guess_none PASSED                   [ 25%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED            [ 28%]
tests/test_game_logic.py::test_parse_guess_zero PASSED                   [ 31%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED        [ 34%]
tests/test_game_logic.py::test_parse_guess_special_characters PASSED     [ 37%]
tests/test_game_logic.py::test_parse_guess_large_number PASSED           [ 40%]
tests/test_game_logic.py::test_parse_guess_returns_error_message_on_failure PASSED [ 42%]
tests/test_game_logic.py::test_check_guess_win PASSED                    [ 45%]
tests/test_game_logic.py::test_check_guess_too_high_outcome PASSED       [ 48%]
tests/test_game_logic.py::test_check_guess_too_high_hint_says_lower PASSED [ 51%]
tests/test_game_logic.py::test_check_guess_too_low_outcome PASSED        [ 54%]
tests/test_game_logic.py::test_check_guess_too_low_hint_says_higher PASSED [ 57%]
tests/test_game_logic.py::test_check_guess_secret_always_int PASSED      [ 60%]
tests/test_game_logic.py::test_check_guess_one_above_secret PASSED       [ 62%]
tests/test_game_logic.py::test_check_guess_one_below_secret PASSED       [ 65%]
tests/test_game_logic.py::test_check_guess_at_range_minimum PASSED       [ 68%]
tests/test_game_logic.py::test_check_guess_large_values PASSED           [ 71%]
tests/test_game_logic.py::test_update_score_win_first_attempt PASSED     [ 74%]
tests/test_game_logic.py::test_update_score_win_minimum_points PASSED    [ 77%]
tests/test_game_logic.py::test_update_score_too_high_deducts_points PASSED [ 80%]
tests/test_game_logic.py::test_update_score_too_high_even_attempt_no_bonus PASSED [ 82%]
tests/test_game_logic.py::test_update_score_too_high_odd_attempt_deducts PASSED [ 85%]
tests/test_game_logic.py::test_update_score_too_low_deducts_points PASSED [ 88%]
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged PASSED [ 91%]
tests/test_game_logic.py::test_update_score_score_can_go_negative PASSED [ 94%]
tests/test_game_logic.py::test_update_score_win_at_minimum_clamp_boundary PASSED [ 97%]
tests/test_game_logic.py::test_update_score_win_just_above_minimum PASSED [100%]

============================= 35 passed in 0.04s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
