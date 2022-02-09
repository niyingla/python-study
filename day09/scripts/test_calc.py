# 1.导包
import pytest

from day09.api.calc import add


# 2.定义测试类


class TestAdd(object):
    """测试加法类"""

    # 3.定义测试方法
    def test01_add(self):  # 自动导包键 all + enter
        # 3.1 调用被测函数
        result = add(1, 2)
        # 3.2 打印结果
        print(f"计算结果为{result}")

    # # 包含负数的
    # 3.定义测试方法
    def test02_add(self):  # 自动导包键 all + enter
        # 3.1 调用被测函数
        result = add(-1, 2)
        # 3.2 打印结果
        print(f"计算结果为{result}")

    # 测试小数的
    # 3.定义测试方法
    def test03_add(self):  # 自动导包键 all + enter
        # 3.1 调用被测函数
        result = add(2, 124.45678)
        # 3.2 打印结果
        print(f"计算结果为{result}")

if __name__ == '__main__':
    pytest.main(['-s', "test_calc.py"])


