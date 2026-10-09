def remaining(capacity, registered):
    return capacity - registered

def test_remaining():
    assert remaining(20, 8) == 12
    assert remaining(5, 5) == 0

test_remaining() 
