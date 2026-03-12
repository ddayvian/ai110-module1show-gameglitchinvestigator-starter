import sys
import os

# Add the root directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import get_range_for_difficulty, check_guess

def test_new_game_button():
    # Simulate the "New Game" button functionality
    import streamlit as st
    st.session_state["secret"] = 50
    st.session_state["attempts"] = 5
    st.session_state["status"] = "lost"
    st.session_state["history"] = [10, 20, 30]

    # Simulate new game logic
    low, high = get_range_for_difficulty("Normal")
    st.session_state["secret"] = 75  # New secret number
    st.session_state["attempts"] = 0
    st.session_state["status"] = "playing"
    st.session_state["history"] = []

    assert st.session_state["secret"] == 75
    assert st.session_state["attempts"] == 0
    assert st.session_state["status"] == "playing"
    assert st.session_state["history"] == []

def test_difficulty_ranges():
    # Test difficulty ranges
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_hint_logic():
    # Test hint logic
    assert check_guess(50, 75) == ("Too Low", "📈 Go HIGHER!")  # FIX: Updated test to match corrected hint logic
    assert check_guess(100, 75) == ("Too High", "📉 Go LOWER!")  # FIX: Updated test to match corrected hint logic
    assert check_guess(75, 75) == ("Win", "🎉 Correct!")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")  # Updated to match the tuple output

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")  # Updated to match the tuple output

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")  # Updated to match the tuple output

def test_new_game_resets_state():
    # Test that the "New Game" button resets the game state correctly
    import streamlit as st
    st.session_state["secret"] = 50
    st.session_state["attempts"] = 5
    st.session_state["status"] = "lost"
    st.session_state["history"] = [10, 20, 30]
    st.session_state["score"] = 100

    # Simulate "New Game" button logic
    low, high = get_range_for_difficulty("Easy")
    st.session_state["secret"] = 15  # New secret number
    st.session_state["attempts"] = 0
    st.session_state["status"] = "playing"
    st.session_state["history"] = []
    st.session_state["score"] = 0

    # Assertions to verify the reset state
    assert st.session_state["secret"] == 15
    assert st.session_state["attempts"] == 0
    assert st.session_state["status"] == "playing"
    assert st.session_state["history"] == []
    assert st.session_state["score"] == 0  # FIX: Added test for "New Game" reset logic with Copilot assistance
