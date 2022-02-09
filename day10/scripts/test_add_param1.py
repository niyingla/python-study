# encoding:utf-8
import pytest

from day10.api.add import add

# 定义一个构造测试数据
def build_data():
    data = [(1, 2, 3), (1, -1, 0), (1, 0.1, 1.1)]
    return data


class TestAdd(object):
    """测试加法类"""

    @pytest.mark.parametrize("x,y,expect", build_data())
    def test01_add(self, x, y, expect):
        result = add(x, y)
        print(f"计算结果为{result}")
        assert result == expect
