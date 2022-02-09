# encoding:utf-8
import pytest
import time


class TestDemo(object):
    def setup_class(self):
        print("开始时间=", time.time())
        time.sleep(1)

    def teardown_class(self):
        print("结束时间=", time.time())

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')


if __name__ == '__main__':
    pytest.main(["-s", "hm_02setup_class和teardown_class的引入.py"])
