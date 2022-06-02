import os


def test_loaded_testing_env():
    """
    Test if test.env was loaded.
    """
    assert os.getenv("TESTING") == "true"
