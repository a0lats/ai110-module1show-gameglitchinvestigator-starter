from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


# --- check_guess tests ---

def test_correct_guess_returns_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high_returns_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # FIX verification: message must say lower, not higher

def test_guess_too_low_returns_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message  # FIX verification: message must say higher

# --- parse_guess tests ---

def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert not ok
    assert val is None

def test_parse_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok
    assert val == 42

def test_parse_float_string_truncates():
    ok, val, err = parse_guess("7.9")
    assert ok
    assert val == 7

def test_parse_non_number():
    ok, val, err = parse_guess("abc")
    assert not ok

# --- update_score tests ---

def test_win_score_increases():
    score = update_score(0, "Win", 1)
    assert score > 0

def test_wrong_guess_deducts_points():
    score = update_score(50, "Too High", 2)
    assert score < 50
    score = update_score(50, "Too Low", 3)
    assert score < 50

# --- get_range_for_difficulty tests ---

def test_hard_range_is_harder_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high  # Hard should be a wider range