import pytest
import json

with open('tpshop.json', encoding='utf-8') as f:
    info = json.load(f)


class TestShop(object):
    def test01(self):
        assert info.get('msg') == '登陆成功'

    def test02(self):
        assert info.get('result').get('mobile') == '18903776820'


if __name__ == '__main__':
    pytest.main(['-s', 'hm.py'])
