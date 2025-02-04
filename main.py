import pytest


def run_tests():
    pytest.main(["tests/test_first.py", "tests/test_second.py", "tests/test_third.py"])


if __name__ == "__main__":
    run_tests()

