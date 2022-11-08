from unittest import mock
import pytest

from sample import guess_number, get_ip

@pytest.mark.parametrize("input, expected", [(3, "You won!"),(4, "You lost!")])
@mock.patch("sample.roll_dice")
def test_guess_number(mock_roll_dice, input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(input) == expected
    mock_roll_dice.assert_called_once()

@mock.patch("sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                                **{"status_code":200,"json.return_value": {"origin":"0.0.0.0"}})
    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")
    