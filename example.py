def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def subtract(a, b):
    return a - b

def test_subtract(a, b):
    assert subtract(5, 1) == 4