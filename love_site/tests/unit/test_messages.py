import pytest
from unittest.mock import patch, mock_open
from app.services.messages import load_messages, personalize_messages


def test_load_messages_returns_list():
    """Test that load_messages returns a list."""
    with patch('builtins.open', mock_open(read_data='{"messages": [{"id": 1, "text": "Test"}]}')):
        msgs = load_messages()
        assert isinstance(msgs, list)


def test_load_messages_with_valid_data():
    """Test loading valid data."""
    data = '{"messages": [{"id": 1, "text": "Hello {lover}"}]}'
    with patch('builtins.open', mock_open(read_data=data)):
        msgs = load_messages()
        assert len(msgs) == 1
        assert msgs[0]['text'] == 'Hello {lover}'


def test_load_messages_file_not_found():
    """Test handling file not found."""
    with patch('builtins.open', side_effect=FileNotFoundError):
        msgs = load_messages()
        assert msgs == []


def test_load_messages_invalid_json():
    """Test handling invalid JSON."""
    with patch('builtins.open', mock_open(read_data='invalid json')):
        msgs = load_messages()
        assert msgs == []


def test_personalize_messages():
    """Test message personalization."""
    messages = [
        {"id": 1, "text": "Hello {lover}"},
        {"id": 2, "text": "From {sender}"}
    ]
    result = personalize_messages(messages, "Alice", "Bob")
    assert result[0]['text'] == "Hello Alice"
    assert result[1]['text'] == "From Bob"


def test_personalize_messages_empty_lover():
    """Test personalization with empty lover."""
    messages = [{"id": 1, "text": "Hello {lover}"}]
    result = personalize_messages(messages, "", "Bob")
    assert result[0]['text'] == "Hello my love"


def test_personalize_messages_default_sender():
    """Test default value for sender."""
    messages = [{"id": 1, "text": "From {sender}"}]
    result = personalize_messages(messages, "Alice")
    assert result[0]['text'] == "From Djochrist"
