import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---
# Bug fixed: Hard was 1-50 (easier than Normal 1-100); corrected to 1-200

def test_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_difficulty_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_difficulty_hard_is_wider_than_normal():
    low, high = get_range_for_difficulty("Hard")
    assert high > 100, "Hard difficulty should have a wider range than Normal (1-100)"

def test_difficulty_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 200)

def test_difficulty_unknown_returns_default():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_decimal_rounds_to_int():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_guess_zero():
    ok, value, err = parse_guess("0")
    assert ok is True
    assert value == 0

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_parse_guess_special_characters():
    ok, value, err = parse_guess("!@#")
    assert ok is False
    assert value is None

def test_parse_guess_large_number():
    ok, value, err = parse_guess("999999")
    assert ok is True
    assert value == 999999

def test_parse_guess_returns_error_message_on_failure():
    _, _, err = parse_guess("abc")
    assert err is not None and len(err) > 0


# --- check_guess ---
# Bug fixed: "Go HIGHER" and "Go LOWER" hints were swapped

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high_outcome():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_high_hint_says_lower():
    # Bug: previously returned "Go HIGHER!" when guess was too high
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, "When guess is too high, hint should say Go LOWER"

def test_check_guess_too_low_outcome():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_too_low_hint_says_higher():
    # Bug: previously returned "Go LOWER!" when guess was too low
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, "When guess is too low, hint should say Go HIGHER"

def test_check_guess_secret_always_int():
    # Bug: secret was cast to str on even attempts, causing broken comparisons like "9" > "10"
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low", "Integer comparison: 9 < 10 should be Too Low, not a string comparison error"

def test_check_guess_one_above_secret():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_check_guess_one_below_secret():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_check_guess_at_range_minimum():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_check_guess_large_values():
    outcome, _ = check_guess(200, 100)
    assert outcome == "Too High"


# --- update_score ---
# Bug fixed: even-attempt Too High guesses awarded +5; should always deduct 5

def test_update_score_win_first_attempt():
    score = update_score(0, "Win", 1)
    assert score == 80  # 100 - 10*(1+1) = 80

def test_update_score_win_minimum_points():
    score = update_score(0, "Win", 20)
    assert score == 10  # capped at minimum 10

def test_update_score_too_high_deducts_points():
    score = update_score(50, "Too High", 2)
    assert score == 45, "Too High should always deduct 5 points"

def test_update_score_too_high_even_attempt_no_bonus():
    # Bug: even attempts for Too High previously awarded +5 instead of -5
    score = update_score(50, "Too High", 2)
    assert score < 50, "Wrong guess should never award points"

def test_update_score_too_high_odd_attempt_deducts():
    score = update_score(50, "Too High", 3)
    assert score == 45

def test_update_score_too_low_deducts_points():
    score = update_score(50, "Too Low", 1)
    assert score == 45

def test_update_score_unknown_outcome_unchanged():
    score = update_score(50, "Something", 1)
    assert score == 50

def test_update_score_score_can_go_negative():
    score = update_score(3, "Too Low", 1)
    assert score == -2

def test_update_score_win_at_minimum_clamp_boundary():
    # attempt 9: 100 - 10*(9+1) = 0, should clamp to minimum 10
    score = update_score(0, "Win", 9)
    assert score == 10

def test_update_score_win_just_above_minimum():
    # attempt 8: 100 - 10*(8+1) = 10, exactly at minimum — no clamp needed
    score = update_score(0, "Win", 8)
    assert score == 10
