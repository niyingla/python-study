import pytest

from day10.api.sub import sub
from day10.data.data import build1_data


class TestSub(object):
    """测试减法类"""

    @pytest.mark.parametrize("x,y,expect", build1_data())
    def test01_sub(self, x, y, expect):
        result = sub(x, y)
        print(f"结算结果为{result}")
        assert result == expect
