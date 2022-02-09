# encoding:utf-8
import pytest

from day10.api.add import add


class TestAdd(object):
    """测试加法类"""

    @pytest.mark.parametrize("x,y,expect", [(1, 2, 3), (1, -1, 0),(1, 0.1, 1.1)])
    def test01_add(self, x, y, expect):
        result = add(x, y)
        print(f"计算结果为{result}")
        assert result == expect
