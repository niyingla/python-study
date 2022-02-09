# encoding:utf-8
import pytest

from day11.api.div import div
from day11.data.data import build_data1


class TestDiv(object):
    @pytest.mark.parametrize('x,y,expect', build_data1())
    def test_div(self, x, y, expect):
        result = div(x, y)
        print(f"计算的和为{result}")
        assert result == expect
