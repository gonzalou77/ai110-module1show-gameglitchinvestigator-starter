def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """
    Return the (low, high) inclusive number range for a given difficulty.

    Easy   -> (1, 20):  small range, easiest to guess
    Normal -> (1, 100): standard range
    Hard   -> (1, 200): widest range, hardest to guess
    Any unrecognised difficulty falls back to the Normal range (1, 100).
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str | None) -> tuple[bool, int | None, str | None]:
    """
    Validate and convert raw text input from the user into an integer guess.

    Accepts whole numbers and decimals (truncated to int, e.g. "7.9" -> 7).
    Rejects empty input, None, and non-numeric strings.

    Returns a three-element tuple:
      - ok (bool):              True if parsing succeeded, False otherwise
      - guess_int (int | None): the parsed integer, or None on failure
      - error_msg (str | None): human-readable error string, or None on success
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare the player's guess against the secret number.

    Returns a two-element tuple:
      - outcome (str): one of "Win", "Too High", or "Too Low"
      - message (str): an emoji-prefixed hint shown to the player

    "Too High" means the guess was above the secret -> player should go lower.
    "Too Low"  means the guess was below the secret -> player should go higher.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """
    Calculate and return the new score after a guess.

    Win:
      Awards 100 - 10 * (attempt_number + 1) points, minimum 10.
      Fewer attempts used means a higher score.

    Too High / Too Low:
      Deducts 5 points. Wrong guesses never award points.
      Score can go negative if the player guesses poorly enough.

    Any unrecognised outcome leaves the score unchanged.
    """
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score
