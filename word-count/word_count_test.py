# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/word-count/canonical-data.json
# File last updated on 2023-07-19

import pytest

from word_count import count_words  # adjust the import path to your module

# ---------------------------------------------------------------
# 1. Basic tests
# ---------------------------------------------------------------


def test_empty_string():
    assert count_words("") == {}


def test_single_word():
    assert count_words("word") == {"word": 1}


def test_single_word_lowercase():
    assert count_words("word") == {"word": 1}


def test_two_unique_words():
    assert count_words("one two") == {"one": 1, "two": 1}


def test_two_words_with_multiple_spaces():
    assert count_words("one   two") == {"one": 1, "two": 1}


def test_multiple_occurrences_of_a_word():
    assert count_words("one one two") == {"one": 2, "two": 1}


def test_case_insensitive():
    assert count_words("You come back, you hear me? DO YOU HEAR ME?") == {
        "you": 3,
        "come": 1,
        "back": 1,
        "hear": 2,
        "me": 2,
        "do": 1,
    }


# ---------------------------------------------------------------
# 2. Punctuation as separators
# ---------------------------------------------------------------


def test_punctuation_as_separator():
    assert count_words("one,two") == {"one": 1, "two": 1}


def test_various_punctuation():
    assert count_words("one.two!three?four;five:six") == {
        "one": 1,
        "two": 1,
        "three": 1,
        "four": 1,
        "five": 1,
        "six": 1,
    }


def test_punctuation_and_spaces():
    assert count_words("one, two, three.") == {"one": 1, "two": 1, "three": 1}


def test_question_and_exclamation():
    assert count_words("What? Really?! Yes!") == {
        "what": 1,
        "really": 1,
        "yes": 1,
    }


def test_parentheses_and_brackets():
    assert count_words("Hello (world) [again]") == {
        "hello": 1,
        "world": 1,
        "again": 1,
    }


def test_quotes_are_separators():
    assert count_words("He said \"hello\" and 'bye'") == {
        "he": 1,
        "said": 1,
        "hello": 1,
        "and": 1,
        "bye": 1,
    }


def test_leading_and_trailing_punctuation():
    assert count_words("...word!!!") == {"word": 1}


def test_only_punctuation():
    assert count_words("...!?") == {}


def test_dashes_and_underscores():
    assert count_words("well-known_thing") == {
        "well": 1,
        "known": 1,
        "thing": 1,
    }


# ---------------------------------------------------------------
# 3. Whitespace as separators
# ---------------------------------------------------------------


def test_newlines():
    assert count_words("one\ntwo\nthree") == {"one": 1, "two": 1, "three": 1}


def test_tabs():
    assert count_words("one\ttwo\tthree") == {"one": 1, "two": 1, "three": 1}


def test_mixed_whitespace():
    assert count_words("one \t two \n three   four") == {
        "one": 1,
        "two": 1,
        "three": 1,
        "four": 1,
    }


def test_multiple_newlines():
    assert count_words("a\n\n\nb") == {"a": 1, "b": 1}


# ---------------------------------------------------------------
# 4. Numbers are words
# ---------------------------------------------------------------


def test_numbers_are_words():
    assert count_words("It costs 100 dollars.") == {
        "it": 1,
        "costs": 1,
        "100": 1,
        "dollars": 1,
    }


def test_multiple_numbers():
    assert count_words("1 2 3 1 2 1") == {"1": 3, "2": 2, "3": 1}


def test_number_with_punctuation():
    assert count_words("(42), 3.14; -7") == {"42": 1, "3": 1, "14": 1, "7": 1}


# ---------------------------------------------------------------
# 5. Apostrophes in contractions (must be kept)
# ---------------------------------------------------------------


def test_basic_contraction():
    assert count_words("they're") == {"they're": 1}


def test_multiple_contractions():
    assert count_words("it's we're they're") == {
        "it's": 1,
        "we're": 1,
        "they're": 1,
    }


def test_contraction_with_repetition():
    assert count_words("it's it's it's") == {"it's": 3}


def test_contraction_case_insensitive():
    assert count_words("It's IT'S it's") == {"it's": 3}


def test_contraction_within_sentence():
    assert count_words("I don't know if it's true") == {
        "i": 1,
        "don't": 1,
        "know": 1,
        "if": 1,
        "it's": 1,
        "true": 1,
    }


def test_multiple_apostrophes_in_word():
    # e.g. "o'clock" or rare forms like "y'all'd've"
    assert count_words("o'clock") == {"o'clock": 1}


def test_contraction_at_end_of_sentence():
    assert count_words("Yes, it's.") == {"yes": 1, "it's": 1}


def test_contraction_at_start_of_sentence():
    assert count_words("'Tis the season") == {"tis": 1, "the": 1, "season": 1}


# ---------------------------------------------------------------
# 6. Apostrophes used as quotes (must act as separators)
# ---------------------------------------------------------------


def test_quoted_word():
    assert count_words("'hello'") == {"hello": 1}


def test_quoted_contraction():
    assert count_words("'can't'") == {"can't": 1}


def test_apostrophe_at_start():
    assert count_words("'hello world'") == {"hello": 1, "world": 1}


def test_apostrophe_at_end():
    assert count_words("hello world'") == {"hello": 1, "world": 1}


def test_apostrophe_between_words():
    assert count_words("hello ' world") == {"hello": 1, "world": 1}


def test_multiple_quotes():
    assert count_words("'a' 'b' 'c'") == {"a": 1, "b": 1, "c": 1}


def test_nested_quotes():
    assert count_words("\"'hello'\"") == {"hello": 1}


# ---------------------------------------------------------------
# 7. Combined and complex cases
# ---------------------------------------------------------------


def test_the_classic_exercism_example():
    sentence = "Joe can't tell between 'large' and large."
    assert count_words(sentence) == {
        "joe": 1,
        "can't": 1,
        "tell": 1,
        "between": 1,
        "large": 2,
        "and": 1,
    }


def test_subtitle_with_contractions_and_punctuation():
    sentence = (
        "I don't know, he said. \"It's not what you think!\" "
        "She's not coming... is she?"
    )
    assert count_words(sentence) == {
        "i": 1,
        "don't": 1,
        "know": 1,
        "he": 1,
        "said": 1,
        "it's": 1,
        "not": 2,
        "what": 1,
        "you": 1,
        "think": 1,
        "she's": 1,
        "coming": 1,
        "is": 1,
        "she": 1,
    }


def test_mixed_contractions_and_quotes():
    sentence = "He said 'don't do it' but it's too late"
    assert count_words(sentence) == {
        "he": 1,
        "said": 1,
        "don't": 1,
        "do": 1,
        "it": 1,
        "but": 1,
        "it's": 1,
        "too": 1,
        "late": 1,
    }


def test_repeated_contraction_and_normal_word():
    sentence = "it's it's not not it's"
    assert count_words(sentence) == {"it's": 3, "not": 2}


def test_apostrophe_only():
    assert count_words("'") == {}


def test_multiple_apostrophes_only():
    assert count_words("'''") == {}


def test_contraction_surrounded_by_punctuation():
    assert count_words("(it's), [they're];") == {"it's": 1, "they're": 1}


def test_long_repeated_subtitle():
    sentence = "No no no! I won't won't won't do it, it's not fair."
    assert count_words(sentence) == {
        "no": 3,
        "i": 1,
        "won't": 3,
        "do": 1,
        "it": 1,
        "it's": 1,
        "not": 1,
        "fair": 1,
    }


def test_all_punctuation_separators():
    # Every punctuation character in `characters` must act as a separator
    sentence = 'a.b!c@d#e$f%g^h&i*j(k)l,m;n:o"p_q-r'
    result = count_words(sentence)
    for letter in "abcdefghijklmnopqr":
        assert result[letter] == 1


def test_uppercase_contraction():
    assert count_words("DON'T SHOUT") == {"don't": 1, "shout": 1}


def test_contraction_with_uppercase_inside():
    assert count_words("I'm OK") == {"i'm": 1, "ok": 1}


# ---------------------------------------------------------------
# 8. Edge cases
# ---------------------------------------------------------------


def test_whitespace_only():
    assert count_words("   \t\n  ") == {}


def test_single_character_word():
    assert count_words("a b c") == {"a": 1, "b": 1, "c": 1}


def test_repeated_single_character():
    assert count_words("a a a a") == {"a": 4}


def test_number_and_word():
    assert count_words("word 1 word 1") == {"word": 2, "1": 2}


def test_leading_trailing_whitespace():
    assert count_words("   hello world   ") == {"hello": 1, "world": 1}


def test_only_numbers():
    assert count_words("1 2 3") == {"1": 1, "2": 1, "3": 1}


def test_contraction_with_number():
    # e.g. "the '90s"
    assert count_words("the '90s") == {"the": 1, "90s": 1}


# ---------------------------------------------------------------
# 9. Parameterized tests for broad coverage
# ---------------------------------------------------------------


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("", {}),
        (" ", {}),
        ("a", {"a": 1}),
        ("A", {"a": 1}),
        ("a a", {"a": 2}),
        ("a, a", {"a": 2}),
        ("a; a", {"a": 2}),
        ("a\ta", {"a": 2}),
        ("a\na", {"a": 2}),
        ("a.a", {"a": 2}),
        ("a-a", {"a": 2}),
        ("a_a", {"a": 2}),
        ("it's", {"it's": 1}),
        ("'it'", {"it": 1}),
        ("'it's'", {"it's": 1}),
        ("it's it's", {"it's": 2}),
        ("1 2 3", {"1": 1, "2": 1, "3": 1}),
        ("Hello, World!", {"hello": 1, "world": 1}),
    ],
)
def test_parameterized_basic(sentence, expected):
    assert count_words(sentence) == expected
