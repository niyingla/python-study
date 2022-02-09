# encoding:utf-8
import pytest

from day10.api.div import div
from day10.data.data import build4_data


class TestDiv(object):
    """测试除法类类"""

    @pytest.mark.parametrize("x,y,expect", build4_data())
    def test01_div(self, x, y, expect):
        result = div(x, y)
        print(f"结算结果为{result}")
        assert result == expect
# 注意事项
# 1,四舍五入函数round(被操作数据,保留小数位,Eugene默认不保留,可以不写保留数
# 2,f格式化输出也是需要保留小数点后的有效位数是.{变量:小数位数f}
