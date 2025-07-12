def test_basic_assertion():
    """Test basic assertion to verify CI is working"""
    assert 1 + 1 == 2


def test_string_operations():
    """Test string operations"""
    test_string = "Hello, World!"
    assert "World" in test_string
    assert test_string.startswith("Hello")


def test_list_operations():
    """Test list operations"""
    test_list = [1, 2, 3, 4, 5]
    assert len(test_list) == 5
    assert 3 in test_list
