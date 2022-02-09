# encoding:utf-8
import pytest

from day10.api.add import add


class TestAdd(object):
    """测试加法类"""

    def test01_add(self):
        result = add(1, 2)
        print(f"计算结果为{result}")
        assert result == 3

    def test02_add(self):
        result = add(1, -1)
        print(f"计算结果为{result}")
        assert result == 0

    def test03_add(self):
        result = add(1, 0.1)
        print(f"计算结果为{result}")
        assert result == 1.1

# if __name__ == '__main__':
#     pytest.main()
