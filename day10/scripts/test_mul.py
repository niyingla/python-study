# encoding:utf-8
import pytest

from day10.api.mul import mul
from day10.data.data import build3_data


class TestMul(object):
    """测试乘法法类"""

    @pytest.mark.parametrize("x,y,expect", build3_data())
    def test01_mul(self, x, y, expect):
        result = mul(x, y)
        print(f"计算结果为{result}")
        assert result == expect
