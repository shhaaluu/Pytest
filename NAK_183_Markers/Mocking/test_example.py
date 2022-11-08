import pytest
from datetime import datetime
from example import get_time_of_day

def test_get_time_of_day(mocker):
    
    mock_now = mocker.patch("example.datetime")
    mock_now.now.return_value = datetime(2016, 5, 20, 14, 10, 0)

    assert get_time_of_day() == "Afternoon"