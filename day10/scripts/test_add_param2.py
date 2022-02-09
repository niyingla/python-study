# encoding:utf-8
import pytest

from day10.api.add import add
from day10.data.data import build_data


class TestAdd(object):
    """测试加法类"""

    @pytest.mark.parametrize("x,y,expect", build_data())
    def test01_add(self, x, y, expect):
        result = add(x, y)
        print(f"计算结果为{result}")
        assert result == expect
