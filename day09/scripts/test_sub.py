# 减法计算


import pytest

from day09.api.sub import sub


class TestSub(object):
    """测试减法类"""

    def test01_sub(self):
        result = sub(4, 2)
        print(f"计算结果为{result}")


if __name__ == '__main__':
    #    pytest.main(['-s', "test_sub.py"])
    pytest.main()
