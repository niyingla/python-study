import pytest
from day09.api.mul import mul


class TestMul(object):
    def test01_mul(self):
        result = mul(2, 3)
        print(f"结果为{result}")


if __name__ == '__main__':
    pytest.main(['-s', 'test_mul.py'])
