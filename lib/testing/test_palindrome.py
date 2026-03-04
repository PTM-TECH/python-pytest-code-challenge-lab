import pytest
from lib.palindrome import longest_palindromic_substring


# Basic Test Cases

@pytest.mark.parametrize("input_str, expected_outputs", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("racecar", ["racecar"]),
])
def test_basic_cases(input_str, expected_outputs):
    result = longest_palindromic_substring(input_str)
    assert result in expected_outputs


# Edge Cases

def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_long_palindrome():
    result = longest_palindromic_substring("abcde")
    assert result in ["a", "b", "c", "d", "e"]


# Numeric Input Cases

def test_numeric_palindrome():
    assert longest_palindromic_substring("12321") == "12321"


def test_numeric_no_palindrome():
    result = longest_palindromic_substring("12345")
    assert result in ["1", "2", "3", "4", "5"]


# Case Sensitivity

def test_case_sensitive():
    result = longest_palindromic_substring("Aa")
    assert result in ["A", "a"]


# Palindrome in Middle

def test_palindrome_in_middle():
    assert longest_palindromic_substring("xyzracecarabc") == "racecar"


# Palindrome at Beginning

def test_palindrome_at_start():
    assert longest_palindromic_substring("abbaXYZ") == "abba"


# Palindrome at End

def test_palindrome_at_end():
    assert longest_palindromic_substring("XYZabba") == "abba"