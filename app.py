import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

# Maps each difficulty level to the maximum number of guesses allowed.
ATTEMPT_LIMIT_MAP: dict[str, int] = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}

# Page config
# Sets the browser tab title and favicon for the Streamlit app.

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

# Sidebar settings
# Lets the player choose a difficulty before or between games.
# Derives the attempt limit and number range from the chosen difficulty.

st.sidebar.header("Settings")

difficulty: str = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit = ATTEMPT_LIMIT_MAP[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# Session state initialization
# Streamlit reruns the entire script on every interaction, so session_state
# is used to persist game data (secret number, attempt count, score, etc.)
# across reruns. Each key is only initialised once per browser session.

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
if "attempts" not in st.session_state:
    st.session_state.attempts = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "status" not in st.session_state:
    st.session_state.status = "playing"
if "history" not in st.session_state:
    st.session_state.history = []

# Game UI
# Displays the current range, attempts remaining, and a debug expander.
# Renders the guess input and the three action controls (submit, new game,
# hint toggle) as side-by-side columns.

st.subheader("Make a guess")
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts + 1}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess: str = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# New game handler
# Resets all session state to starting values and picks a new secret number
# within the range for the currently selected difficulty, then reruns the app.

if new_game:
    st.session_state.attempts = 1
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

# Game-over guard
# If the game has already ended (won or lost), show the appropriate message
# and halt further script execution so the guess form is not rendered.

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

# Guess submission handler
# Increments the attempt counter, validates the input via parse_guess, then
# checks the guess and updates the score. Ends the game when the player wins
# or exhausts their allowed attempts.

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        assert guess_int is not None
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
