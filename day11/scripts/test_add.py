# encoding:utf-8
import pytest

from day11.api.add import add
from day11.data.data import build_data


class TestAdd(object):
    @pytest.mark.parametrize("x,y,expect", build_data())
    def test_add(self, x, y, expect):
        result = add(x, y)
        print(f'计算结果为{result}')
        assert result == expect



