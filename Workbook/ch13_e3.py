import pytest

@pytest.fixture
def record():
    return{"title": "python", "capcity":20}

def test_record_capcity(record):
    assert record["capcity"] == 20
    
