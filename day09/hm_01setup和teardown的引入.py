# encoding:utf-8
import pytest
import time


class TestTime(object):
    def setup(self):
        print("start time=", time.time())
        time.sleep(1)

    def teardown(self):
        print("end time=", time.time())


    def test01(self):
        print("test01")

    def test02(self):
        print("test02")


if __name__ == '__main__':
    pytest.main(['-s', 'hm_01setup和teardown的引入.py'])
