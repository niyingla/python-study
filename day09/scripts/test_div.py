from day09.api.div import div
import pytest


class TestDiv(object):
    """测试除法类"""

    def test01_div(self):
        """除法方法"""
        result = div(44555, 2443)
        print(f"结果为{result}")
        assert result == 18.2378223495702
        assert 'a' in 'admin'  # 断言包含关系
        # assert 'as' in 'admin' # 断言as不在admin中
        assert result != 0  # 断言为真(非0的数据为真:True)
        assert result == 0  # 断言为假(0的数据为假:False)


if __name__ == '__main__':
    pytest.main(['-s', 'test_div.py'])
