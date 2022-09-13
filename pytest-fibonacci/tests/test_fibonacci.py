# todo create basic tests with parametrize

import pytest
import basic


class TestFibonacci:
    @pytest.mark.parametrize('number, result', [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3)])
    def test_fibonacci_should_return_expected_output(self, number, result):
        assert basic.fibonacci_recursive(number) == result
