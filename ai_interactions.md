# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

can you add additional linting, describing what each function and block of code does at a high level? Then add it to the AddedLinting.txt file along with the prompt output log

**What did the agent do?**

The AI added more linting but at a higher level to the scripts and then added them to a separate output .txt file.

**What did you have to verify or fix manually?**

I verified that everything was exported correctly to the .txt file logs by opening and reading them, then checking the .py files themselves.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |

Prompt Used:
now that we have fixed the bugs, lets generate pytest cases for them. Could you put the pytest cases in test_game_logic.py in the tests folder?

35/35 passing. Here's what was added for edge cases:

parse_guess (5 new):

"0" — valid zero input
"-5" — negative numbers are parseable
"!@#" — special characters rejected
"999999" — large numbers accepted
Error message is non-empty on failure
check_guess (4 new):

Off-by-one: guess = secret + 1 → Too High
Off-by-one: guess = secret − 1 → Too Low
Boundary at range minimum (1 vs 1 → Win)
Large value gap (200 vs 100 → Too High)
update_score (3 new):

Score can go negative (3 − 5 = −2)
Win at attempt 9 clamps to minimum 10 (would be 0 without clamp)
Win at attempt 8 lands exactly at 10 (boundary, no clamp needed)

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

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
how well does the code in the .py files in this repository comply with PEP 8 style?

can you export the prompt results of the linting and the PEP8style fixes to a PEP8_LintingPromptingChanges.txt?

can you add additional linting, describing what each function and block of code does at a high level? Then add it to the AddedLinting.txt file along with the prompt output log
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

Changes can be found in PEP8_LintingPromptingChanges.txt and AddedLinting.txt

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
