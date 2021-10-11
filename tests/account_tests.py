from pypi_org.viewmodels.account import RegisterViewModel


def test_example():
    assert 1 + 4 == 4

def test_register_validation_when_valid():
    # 3 As of testing - arrange, act and assert
    # arrange
    vm = RegisterViewModel