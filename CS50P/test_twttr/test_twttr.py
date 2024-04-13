from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"
    assert shorten("Python") == "Pythn"
    # Add more test cases for words with no vowels

def test_shorten_with_vowels():
    assert shorten("education") == "dctn"
    assert shorten("Artificial") == "rtfcl"
    # Add more test cases for words with vowels

def test_shorten_empty_string():
    assert shorten("") == ""
    # Add more test cases for an empty string

def test_shorten_mixed_case():
    assert shorten("MixEdCaSe") == "MxdCS"

def test_num():
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"

def test_punc():
    assert shorten("h@llo w*rld!!!") == "h@ll w*rld!!!"
