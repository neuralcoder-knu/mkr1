import pytest
import tempfile
from main import count

@pytest.fixture
def sample_text():
    return "Test1! Te st 5. Test442 Test?"

@pytest.fixture
def temp_file(sample_text):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(sample_text)
    yield temp_file.name

    import os
    os.unlink(temp_file.name)

@pytest.mark.parametrize("text, expected_words, expected_sentences", [
    ("Test1! Te st 5. Test442 Test?", 6, 3),
])
def test_count_words_and_sentences(text, expected_words, expected_sentences, temp_file):
    words, sentences = count(temp_file)
    assert words == expected_words
    assert sentences == expected_sentences

def test_count_words_and_sentences_with_fixture(sample_text, temp_file):
    words, sentences = count(temp_file)
    assert words == 6
    assert sentences == 3