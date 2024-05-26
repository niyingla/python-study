import os


class Student:
    name: str
    age: int

    def __init__(self, **args):
       setattr(self, '__dict__', args)

    def __str__(self):
        return f"name:{self.name},age:{self.age}"


import json

if __name__ == '__main__':
    json_str = '{"name": "huohuo", "age": 18}'
    loads = json.loads(json_str)
    # 赋值字段到对象
    student = Student(**loads)
    print(student.__module__)
