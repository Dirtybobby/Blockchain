import pytest



@pytest.fixture()
def print_some():
    print("some text")
    yield
    print("after_test_print")


@pytest.fixture(scope="session")
def print_before():
    print("before all")

@pytest.mark.skip("Because i was")
def skip_test():
    print("test is skipped")



def test_first(print_some):
    print("First")


def test_second():
    print("second")


def test_third(print_some, print_before):
    print("third")


